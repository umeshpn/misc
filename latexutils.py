import re

DEFN_RE = re.compile(r'^\s*\\newcommand{\\([^}]+)}')
CALL_RE = re.compile(r'\\([a-zA-Z]+)(.*)')
class LaTeXUtils:
    def list_unused_macros(self, macro_file, source_file):
        macro_set = set()
        with open(macro_file, 'r') as macro_fp:
            for line in macro_fp.readlines():
                line = line[:-1]
                m = DEFN_RE.match(line)
                if m:
                    macro_set.add(m.group(1))

        source_map = dict()
        with open(source_file, 'r') as source_fp:
            for line in source_fp.readlines():
                line = line[:-1]
                m = CALL_RE.search(line)
                while m:
                    macro = m.group(1)
                    if macro in source_map:
                        source_map[macro] += 1
                    else:
                        source_map[macro] = 1
                    line = m.group(2)
                    m = CALL_RE.search(line)
        # extra_macros = macro_set - source_map
        # for macro in sorted(extra_macros):
        #     print(macro)

        for macro in macro_set:
            if macro in source_map and source_map[macro] > 1:
                print('%-40s %3d' % (macro, source_map[macro]))



if __name__ == '__main__':
    lu = LaTeXUtils()
    dir = '/Users/umesh.nair/workday-git/umesh-repo/tex/workday/oms-priv/features/OMSDI-127-User-Activity-Filter-Multiple'
    lu.list_unused_macros("%s/%s" %  (dir, 'OMSDI-127-macros.tex'), "%s/%s" %  (dir, 'OMSDI-127-analysis.tex'))



