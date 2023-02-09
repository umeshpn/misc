import re
import math

LETTER_RE = re.compile(r'^\\Letter{(.+)}{(.+)}')
SLOKAM_RE = re.compile(r'^\\begin{.+slokam}{([^}]+)}{([^}]+)}')
var_re = re.compile('\\\\(\S+)')
people_re = re.compile('^\\\\newcommand{\\\\(\S+)}\{(.+)\}')
meter_re = re.compile('^\\\\newcommand{\\\\(\S+)}{\\\\Vruththam{(.+)}}')
N_PEOPLE = 42
numbers = [
    'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
    'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'TwentyOne',
    'TwentyTwo', 'TwentyThree', 'TwentyFour', 'TwentyFive', 'TwentySix', 'TwentySeven', 'TwentyEight', 'TwentyNine',
    'Thirty', 'ThirtyOne', 'ThirtyTwo', 'ThirtyThree', 'ThirtyFour', 'ThirtyFive', 'ThirtySix', 'ThirtySeven',
    'ThirtyEight', 'ThirtyNine', 'Forty', 'FortyOne', 'FortyTwo'
]

class SlokamStatsGenerator:
    def __init__(self, infile, outfile, people_file, meter_file):
        self.infile = infile
        self.outfile = outfile
        self.slok_count = dict()
        self.slok_order = dict()
        self.persons = dict()
        self.meters = dict()
        self.meter_map = dict()
        self.poet_map = dict()
        self.n_slokams = 0
        self.read_people(people_file)
        self.read_meter(meter_file)
        self.pers_number_dict = dict()
        for i in range(len(numbers)):
            pers_name = '\\P%s' % numbers[i]
            self.pers_number_dict[pers_name] = i
        self.person_round_map = ['dummy']
        for i in range(N_PEOPLE):
            self.person_round_map.append(set())
        self.max_rounds = 0
        self.latest_person = 0
        self.meter_round_counts = [
            ['\\VSr', 5],
            ['\\VKm', 5],
            ['\\VSv', 5]
        ]
        self.slok_counts = dict()

    def real_name(self, name):
        m = var_re.match(name)
        if m:
            return self.poet_map[m.group(1)]
        else:
            return name

    def real_meter(self, name):
        m = var_re.match(name)
        if m:
            return self.meter_map[m.group(1)]
        else:
            return name

    def read_people(self, people_file_name):
        with open(people_file_name) as p:
            line = p.readline()
            while line:
                m = people_re.match(line)
                if m:
                    self.poet_map[m.group(1)] = m.group(2)
                line = p.readline()

    def read_meter(self, meter_file_name):
        with open(meter_file_name) as p:
            line = p.readline()
            while line:
                m = meter_re.match(line)
                if m:
                    self.meter_map[m.group(1)] = m.group(2)
                line = p.readline()

    def process(self):
        with open(self.infile, 'r') as inf:
            self.n_slokams = 0
            last_third = None
            last_round = 0
            person_number = 100
            last_person_number = person_number
            for line in inf.readlines():
                line = line[:-1]
                m = LETTER_RE.match(line)
                if m:
                    self.n_slokams += 1
                    first, third = m.group(1), m.group(2)

                    if last_third is not None and last_third != first:
                        print("Previous third letter %s not matching with first letter %s for slokam %d" % (
                        last_third, first, self.n_slokams))
                    last_third = third
                    slok_count_key = first
                    if slok_count_key in self.slok_count:
                        self.slok_count[slok_count_key] = self.slok_count[slok_count_key] + 1
                    else:
                        self.slok_count[slok_count_key] = 1

                    slok_order_key = '%s $\\to$ %s' % (first, third)
                    if slok_order_key in self.slok_order:
                        self.slok_order[slok_order_key] = self.slok_order[slok_order_key] + 1
                    else:
                        self.slok_order[slok_order_key] = 1
                    continue

                m = SLOKAM_RE.match(line)
                if m:
                    person, meter = self.real_name(m.group(1)), self.real_meter(m.group(2))
                    person_number = self.pers_number_dict[m.group(1)]
                    if person_number < last_person_number:
                        last_round += 1
                    person_round_info = self.person_round_map[person_number]
                    person_round_info.add(last_round)
                    self.slok_counts[last_round] =  self.slok_counts.get(last_round, 0) + 1
                    if person in self.persons:
                        self.persons[person] = self.persons[person] + 1
                    else:
                        self.persons[person] = 1
                    if meter in self.meters:
                        self.meters[meter] = self.meters[meter] + 1
                    else:
                        self.meters[meter] = 1
                last_person_number = person_number
                self.latest_person = person_number

        self.max_rounds = last_round
        with open(self.outfile, 'w') as outf:
            outf.write('%s: %d' % ('മൊത്തം ശ്ലോകങ്ങൾ', self.n_slokams))
            self.print_meter_counts(outf)
            self.print_letter_counts(outf)
            self.print_letter_order_counts(outf, lambda x: (-self.slok_order[x], x), 'അക്ഷരക്രമം (എണ്ണം അനുസരിച്ച്)')
            self.print_letter_order_counts(outf, lambda x: x, 'അക്ഷരക്രമം (അക്ഷരം അനുസരിച്ച്)')
            self.print_person_counts(outf)


    def print_meter_counts(self, outf):
        sr_no = 0
        total = 0
        outf.write('\\begin{table}[H]\n')
        outf.write('\\centering\n')
        outf.write('\\begin{tabular}{rlrr}\n')
        outf.write('\\hline\n')
        outf.write(
            '\\textbf{%s} & \\textbf{%s} & \\textbf{%s}  & \\textbf{%s}\\\\\n' % ('No.', 'വൃത്തം', 'എണ്ണം', '\\%'))
        outf.write('\\hline\n')
        for meter in sorted(self.meters, key=lambda x: (-self.meters[x], x)):
            sr_no += 1
            count = self.meters[meter]
            outf.write('$%d$ & %s & $%d$ & $%.2f\\%%$ \\\\\n' % (sr_no, meter, count, count * 100.0 / self.n_slokams))
            total += count
        if total != self.n_slokams:
            print('ERROR: Sum of letter count %d does not match with total slokams %d.' % (total, self.n_slokams))

        outf.write('\\hline\n')
        outf.write('\\end{tabular}\n')
        outf.write('\\caption{%s}\n' % 'വൃത്തങ്ങൾ')
        outf.write('\\end{table}\n\n\n')

    def print_person_counts(self, outf):
        n_entries = len(self.persons)
        n_columns = 2
        n_entries_per_column = 21
        excess_in_last_column = n_columns * n_entries_per_column - n_entries
        sr_no = 0
        total = 0
        outf.write('\\begin{table}[H]\n')
        outf.write('\\renewcommand{\\arraystretch}{1.2}\n')
        # outf.write('\\small\n')
        outf.write('\\centering\n')
        outf.write('\\begin{tabular}{cc}\n')
        outf.write('\\hline\n')
        col_no = 0
        entry_no = 0
        last_count = 0
        for person in sorted(self.persons, key=lambda x: (-self.persons[x], x)):
            if entry_no == 0:
                outf.write('\\begin{tabular}{rlr}\n')
                outf.write(
                    '\\textbf{%s} & \\textbf{%s} & \\textbf{%s}  \\\\\n' % ('No.', 'കവി', 'എണ്ണം'))
                outf.write('\\hline\n')
                # outf.write(' & & & \\\\\n')
            entry_no += 1
            sr_no += 1
            count = self.persons[person]
            if count != last_count:
                outf.write('*%d & %s & $%d$ \\\\\n' % (sr_no, person, count))
            else:
                outf.write('%d & %s & $%d$ \\\\\n' % (sr_no, person, count))
            last_count = count
            total += count

            if sr_no == n_entries:
                for i in range(excess_in_last_column):
                    outf.write(' & & \\\\\n')
                # outf.write(' & & & \\\\\n')
                outf.write('\\end{tabular}\\\\\n')

            elif entry_no == n_entries_per_column:
                # outf.write(' & & & \\\\\n')
                outf.write('\\end{tabular}\n')
                col_no += 1
                if col_no < n_columns:
                    outf.write(' & \n')
                entry_no = 0
        if total != self.n_slokams:
            print('ERROR: Sum of letter count %d does not match with total slokams %d.' % (total, self.n_slokams))

        outf.write('\\hline\n')
        outf.write('\\end{tabular}\n')
        outf.write('\\caption{%s}\n' % 'കവികളും ചൊല്ലിയ ശ്ലോകങ്ങളും')
        outf.write('\\end{table}\n')

        meter_round_pages = (len(self.meter_round_counts) + 1) // 2
        total = 0

        for mr_page in range(meter_round_pages):
            outf.write('\\begin{table}[H]\n')
            #outf.write('\\renewcommand{\\arraystretch}{1.1}\n')
            outf.write('\\begin{tabular}{|r|l|')
            rounds_in_this_page = self.max_rounds - mr_page * 10
            if rounds_in_this_page > 10:
                rounds_in_this_page = 10
            first_round_in_page = mr_page * 10 + 1
            last_round_in_page = mr_page * 10 + 10
            if last_round_in_page > self.max_rounds:
                last_round_in_page = self.max_rounds

            for i in range(1, rounds_in_this_page+1):
                outf.write('c|')
            if mr_page == meter_round_pages - 1:
                outf.write('r|')
            outf.write('}\n')
            outf.write('\\hline\n')
            outf.write('\\textbf{No.} & \\textbf{കവി}')
            columns = 0
            page = 0
            first_meter = (first_round_in_page  - 1) // 5
            last_meter = (last_round_in_page - 1) // 5
            for i in range(first_meter, last_meter+1):
                meter_round = self.meter_round_counts[i]
                outf.write(' & \\multicolumn{%d}{c|}{\\textbf{%s}}\n' % (meter_round[1], meter_round[0]))
                columns += meter_round[1]
            if mr_page == meter_round_pages - 1:
                outf.write('& \\textbf{Total}')
            outf.write('\\\\\n\\cline{3-%d}\n' % (columns + 2))
            outf.write(' & ')
            for i in range(first_round_in_page, last_round_in_page+1):
                outf.write(' & %d ' % i)
            if mr_page == meter_round_pages - 1:
                outf.write(' &  ')
            outf.write('\\\\\n')
            outf.write('\\hline\n')

            for i in range(1, N_PEOPLE+1):
                person_round_info = self.person_round_map[i]
                outf.write('$%d$ & \\P%s' % (i, numbers[i]))
                for j in range(mr_page * 10 + 1 , mr_page * 10 + 1 + rounds_in_this_page):
                    if j in person_round_info:
                        outf.write(' & \\Yes ')
                    elif i > self.latest_person and j == self.max_rounds:
                        outf.write(' &   ')
                    else:
                        outf.write(' &  \\No ')
                if mr_page == meter_round_pages - 1:
                    outf.write(' & $%d$  ' % len(person_round_info))
                outf.write('\\\\\n')

            outf.write('\\hline\n')
            outf.write('&  ')
            for j in range(first_round_in_page, last_round_in_page+1):
                outf.write(' & \\textbf{%d}  ' % self.slok_counts[j])
                total += self.slok_counts[j]

            if mr_page == meter_round_pages - 1:
                outf.write(' & \\textbf{%d} ' % total)
            outf.write('\\\\\n')
            outf.write('\\hline\n')
            outf.write('\\end{tabular}\n')
            outf.write('\\caption{കവികളും ചൊല്ലിയ റൗണ്ടുകളും}\n')
            outf.write('\\end{table}\n')


    def print_letter_counts(self, outf):
        sr_no = 0
        total = 0
        outf.write('\\begin{table}[H]\n')
        outf.write('\\centering\n')
        outf.write('\\begin{tabular}{rcrrr}\n')
        outf.write('\\hline\n')
        outf.write(
            '\\textbf{%s} & \\textbf{%s} & \\textbf{%s} & \\textbf{%s} & \\textbf{%s} \\\\\n' % ('No.', 'അക്ഷരം', 'എണ്ണം', '\\%', "One in"))
        outf.write('\\hline\n')
        for letter in sorted(self.slok_count, key=lambda x: (-self.slok_count[x], x)):
            sr_no += 1
            count = self.slok_count[letter]
            outf.write('$%d$ & %s & $%d$ & $%.2f$ \\%% & $%.2f$ \\\\\n' % (sr_no, letter, count, count * 100.0 / self.n_slokams, self.n_slokams / count))
            total += count
        if total != self.n_slokams:
            print('ERROR: Sum of letter count %d does not match with total slokams %d.' % (total, self.n_slokams))

        outf.write('\\hline\n')
        outf.write('\\end{tabular}\n')
        outf.write('\\caption{%s}\n' % 'അക്ഷരങ്ങൾ')
        outf.write('\\end{table}\n\n\n')

    def print_letter_order_counts(self, outf, sort_order, title):
        max_entries_per_column = 47
        n_entries = len(self.slok_order)
        n_columns = math.ceil(n_entries / max_entries_per_column)
        n_entries_per_column = math.ceil(n_entries / n_columns)
        excess_in_last_column = n_columns * n_entries_per_column - n_entries
        sr_no = 0
        total = 0
        outf.write('\\begin{table}[H]\n')
        outf.write('\\renewcommand{\\arraystretch}{1.2}\n')
        # outf.write('\\small\n')
        outf.write('\\centering\n')
        outf.write('\\resizebox{\\textwidth}{!}{\\begin{tabular}{%s}\n' % ('c' * n_columns))
        outf.write('\\hline\n')
        col_no = 0
        entry_no = 0
        for letter_order in sorted(self.slok_order, key=sort_order):
            if entry_no == 0:
                outf.write('\\begin{tabular}{rcr}\n')
                outf.write(
                    '\\textbf{%s} & \\textbf{%s} & \\textbf{%s}  \\\\\n' % ('No.', 'ക്രമം', '\\#'))
                outf.write('\\hline\n')
                # outf.write(' & & & \\\\\n')
            entry_no += 1
            sr_no += 1
            count = self.slok_order[letter_order]
            outf.write('$%d$ & %s & $%d$ \\\\\n' % (sr_no, letter_order, count))
            total += count

            if sr_no == n_entries:
                for i in range(excess_in_last_column):
                    outf.write(' & & \\\\\n')
                # outf.write(' & & & \\\\\n')
                outf.write('\\end{tabular}\\\\\n')

            elif entry_no == n_entries_per_column:
                # outf.write(' & & & \\\\\n')
                outf.write('\\end{tabular}\n')
                col_no += 1
                if col_no < n_columns:
                    outf.write(' & \n')
                entry_no = 0
        if total != self.n_slokams:
            print('ERROR: Sum of letter count %d does not match with total slokams %d.' % (total, self.n_slokams))

        outf.write('\\hline\n')
        outf.write('\\end{tabular}}\n')
        outf.write('\\caption{%s}\n' % title)
        outf.write('\\end{table}\n')


if __name__ == '__main__':
    in_dir = '/Users/umesh.nair/github-projects/personal-tex/xetex/souparnika-slokams'
    ssg = SlokamStatsGenerator(
        '%s/%s' % (in_dir, 'souparnika-2.tex'),
        '%s/%s' % (in_dir, 'stats.tex'),
        '%s/%s' % (in_dir, 'people.tex'),
        '%s/%s' % (in_dir, 'meter-decl.tex')
    )
    ssg.process()
