import csv
import re

char_map = {
    "\u0d30\u0d4d\u200d" : "\u0d7c",
    "\u0d32\u0d4d\u200d" : "\u0d7d",
    "\u0d28\u0d4d\u200d" : "\u0d7b",
    "\u0d23\u0d4d\u200d" : "\u0d7a",
    "\u0d33\u0d4d\u200d" : "\u0d7e",
    "\u0d4c" : "\u0d57",
    "\u0d7b\u0d4d\u0d31" : "\u0d28\u0d4d\u0d31",
    "\\prash{}" : "\u0d3d"
}

class SouparnikaParser:
    def parse(self, file_name):
        with open(file_name, 'r') as in_file:
            csv_reader = csv.reader(in_file, delimiter=',')
            line_no = 0
            for row in csv_reader:
                line_no += 1
                verse_line = line_no % 5
                meter, number, line, poet = row
                for f, t in char_map.items():
                    line = line.replace(f, t)
                    meter = meter.replace(f, t)
                    poet = poet.replace(f, t)
                if verse_line == 1:
                    print('\\begin{slokam}{%s}{%s}{%s}{}' % (poet, meter, line))
                    print('%s \\\\*' % line)
                elif verse_line == 4:
                    print('%s' % line)
                    print('\\end{slokam}')
                    print('\\Letter{}{}\n')
                elif verse_line > 0:
                    print('%s \\\\*' % line)

if __name__ == '__main__':
    sp = SouparnikaParser()
    sp.parse('/Users/umesh.nair/Downloads/souparnika.csv')


