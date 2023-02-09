import random

class PercentAnalyzer:
    def __init__(self):
        self.values = [.25, .60, .50, .25]

    def do_one_trial(self):
        choice = random.randint(0, 3)