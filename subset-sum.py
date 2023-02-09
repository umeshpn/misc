
class SubsetSumComputer:
    def __init__(self):
        self.sum_map = {0:0, 1:0, 2:0, 3:0, 4:0}
    def analyze(self, n):
        n_perms = 1 << n
        print(n_perms)
        for i in range(n_perms):
            s = self.sum_of_numbers(i, n) % 5
            self.sum_map[s] += 1
        print('\nn = %d : (' % n, end='')
        for key in sorted(self.sum_map):
            print('%8d' % self.sum_map[key], end='')
        print(' )')

    def sum_of_numbers(self, k, n):
        mask = 1
        sum = 0
        numbers = []
        for i in range(n):
            if k & mask != 0:
                numbers.append(i+1)
                sum += (i + 1)
            mask = mask << 1
        # print(k, numbers, sum)
        return sum

if __name__ == '__main__':
    for i in range(0, 40, 5):
        ssc = SubsetSumComputer()
        ssc.analyze(i)





