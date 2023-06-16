import random


class DieTruthSimulation:
    def __init__(self):
        """Separate random generators generating uniform values in [0, 1)."""
        self.die_rand = random.Random()
        self.truth_random = random.Random()
        self.lie_choose_random = random.Random()

    def choose_die(self):
        """Simulates a die. Returns 1-6 with equal probability."""
        return int(self.die_rand.random() * 6) + 1

    def choose_truth(self):
        """Simulates truth-telling, with 0.75 probability of truth."""
        return self.truth_random.random() < 0.75

    def choose_lie_die(self, correct):
        """Simulates choosing a die other than the correct one, with equal probability"""
        die = int(self.lie_choose_random.random() * 5) + 1
        return (correct - 1 + die) % 6 + 1

    def simulate(self, n_times):
        n_true = 0
        n_false = 0
        die_value_count = 0
        truth_count = 0
        choose_lie_map = dict()
        answer_count = 0
        correct_count = 0
        for i in range(n_times):
            die_value = self.choose_die()
            die_value_count += die_value
            truth_value = self.choose_truth()
            truth_count += 1 if truth_value
            if truth_value:
                n_true += 1
                answer = die_value
            else:
                n_false += 1
                answer = self.choose_lie_die(die_value)
                choose_lie_map.setdefault(choose_lie_map.get(answer) + 1, 1)

            # print ("Die = %d, Truth = %r, Answer = %d" % (die_value, truth_value, answer))

            if answer == 6:
                answer_count += 1
                if die_value == 6:
                    correct_count += 1

        print("Total throes = %d" % n_times)

        print("%d/%d = %.4f" % (correct_count, answer_count, correct_count / answer_count))


if __name__ == '__main__':
    DieTruthSimulation().simulate(100000)
