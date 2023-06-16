import re

LINE_RE = re.compile(r'^RETRACT:Start(.+)')


def is_substring_of(s, t):
    return len(s) < len(t) and s in t


def is_superstring_of(s, t):
    return is_substring_of(t, s)


def print_path(path, base_path):
    offset = len(base_path)
    return '%s:  \\Highlight{%s}%s' % (path, base_path, path[offset:])


with open('/Users/umesh/Downloads/hamiltonian.txt') as fp:
    last_path = ''
    base_path = ''
    l = ''
    i = 0
    for line in fp.readlines():
        m = LINE_RE.match(line)
        if m:
            path = m.group(1)
            if is_substring_of(path, last_path):
                l = print_path(last_path, base_path)
                base_path = path
                last_path = path
            elif is_superstring_of(path, last_path):
                print(l)
                last_path = path

            i += 1
            if i == 40:
                break
