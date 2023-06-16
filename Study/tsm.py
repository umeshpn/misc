import re

INPUT_RE = re.compile(r'^(\S+)\s+(\S+)')


class TravelingSalesman:
    def __init__(self):
        self.neigbor_map = dict()
        self.start = 'Start'
        self.end = 'End'
        self.sol_count = 0

    def read_input(self, infile, start='Start', end='End'):
        self.start = start
        self.end = end
        with open(infile, 'r') as neighbors_file:
            for line in neighbors_file.readlines():
                m = INPUT_RE.match(line)
                if m:
                    a, b = m.group(1), m.group(2)
                    self.add_neighbor(a, b)
                    self.add_neighbor(b, a)
        print(self.neigbor_map)

    def add_neighbor(self, a, b):
        if a in self.neigbor_map:
            neighbors = self.neigbor_map.get(a)
        else:
            neighbors = []
            self.neigbor_map[a] = neighbors
        neighbors.append(b)

    def solve(self):
        n_nodes = len(self.neigbor_map)
        seen = set()
        path = []
        seen.add(self.start)
        path.append(self.start)
        self.search(self.start, seen, path)

    def search(self, node, seen, path):
        self.print_path(path, False)
        if node == self.end:
            if len(path) == len(self.neigbor_map):
                self.print_path(path, True)
                return True
            else:
                return False
        for adj in self.neigbor_map[node]:
            if adj in seen:
                continue
            seen.add(adj)
            path.append(adj)
            result = self.search(adj, seen, path)
            # print('\nResult for %s = %s' % (adj, result))
            if result:
                return
            path = path[:-1]
            seen.remove(adj)

    def print_path(self, path, solved):
        self.sol_count += 1
        if solved:
            print("Solution %2d: %s" % (self.sol_count,  '=>'.join(path)))
        else:
            print("Try %s" % '=>'.join(path))


if __name__ == '__main__':
    tsm = TravelingSalesman()
    tsm.read_input('yasar.dat')
    tsm.solve()
