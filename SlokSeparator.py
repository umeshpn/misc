import re

TITLE_RE = re.compile(r'\\DoneSection')
ORIG_START_RE = re.compile(r'\\begin{aslokam}')
ORIG_END_RE = re.compile(r'\\end{aslokam}')
U_START_RE = re.compile(r'\\begin{uslokam}')
U_END_RE = re.compile(r'\\end{uslokam}')


class SlokSeparator:

    def __init__(self):
        self.original = []
        self.kv = []
        self.mv = []
        self.titles = []

    def separate(self, main_file, kv_file, mv_file):
        in_original = False
        in_utrans = False
        with open(main_file, 'r') as main_fp:
            for line in main_fp.readlines():
                line = line[:-1]
                if TITLE_RE.search(line):
                    self.titles.append(line)
                elif ORIG_START_RE.search(line):
                    in_original = True
                    new_orig_slokam = [line]
                elif ORIG_END_RE.search(line):
                    in_original = False
                    self.original.append(new_orig_slokam)

                if in_original:
                    new_orig_slokam.append(line)

        print(len(self.original))
        print(len(self.titles))


if __name__ == '__main__':
    dir = '/Users/umesh/github-projects/personal-tex/xetex/amaruka'
    orig_file = '%s/%s' % (dir, 'amaruka-vema.tex')
    kv_file = '%s/%s' % (dir, 'kv.tex')
    mv_file = '%s/%s' % (dir, 'mv.tex')
    SlokSeparator().separate(orig_file, kv_file, mv_file)