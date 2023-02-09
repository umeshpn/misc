
class LangConverter:
    def __init__(self, char_map):
        self.char_map = char_map

    def convert(self, infile, outfile):
        with open(outfile, 'w') as out_fp:
            with open(infile, 'r') as in_fp:
                for line in in_fp.readlines():
                    line = line[:-1]
                    out_fp.write('%s\n' % self.convert_line(line))

    def convert_line(self, line):
        ret = self.first_pass(line)
        ret = self.second_pass(ret)
        return ret

    def first_pass(self, line):
        ret = ''
        for c in line:
            if c in self.char_map:
                c2 = self.char_map[c]
                if c2:
                    ret += c2
                else:
                    pass
            else:
                ret += c
        return ret

    def second_pass(self, line):
        return line

