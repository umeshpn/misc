import random

class SlapSimulator:
    N_PEOPLE = 1024

    def __init__(self):
        self.slap_dict = None

    def one_slap(self):
        self.init_dict()
        for i in range(self.N_PEOPLE):
            r = random.randint(0, 1)
            if r == 0:
                self.slap_dict[(i+1) % self.N_PEOPLE] = True
            else:
                self.slap_dict[(i - 1) % self.N_PEOPLE] = True

        c = 0
        for b in self.slap_dict:
            if not b:
                c += 1
        return c

    def simulate(self, n_trials):
        s = 0.0
        for i in range(n_trials):
            c = self.one_slap()
            s += c

        print(s / n_trials)

    def init_dict(self):
        self.slap_dict = [False] * self.N_PEOPLE


if __name__ == '__main__':
    s = SlapSimulator()
    s.simulate(10000)
