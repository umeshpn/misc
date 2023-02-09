from abc import ABC, abstractmethod
import random

class FinAdjuster(ABC):
    @staticmethod
    def compute_assets(transactions):
        assets = dict()  # person -> overall money.  +: asset, -: debt
        for t in transactions:
            (from_person, to_person, amount) = t
            assets[from_person] = assets.get(from_person, 0) - amount
            assets[to_person] = assets.get(to_person, 0) + amount
        return assets

    @staticmethod
    def insert_into_desc_list(arr, amount, person):
        index = 0
        while index < len(arr) and arr[index][0] > amount:
            index += 1
        arr.insert(index, (amount, person))

    @staticmethod
    def insert_into_asc_list(arr, amount, person):
        index = 0
        while index < len(arr) and arr[index][0] < amount:
            index += 1
        arr.insert(index, (amount, person))

    def __init__(self):
        self.transactions = None
        self.lenders = None
        self.borrowers = None
        self.adjusted_transactions = None
        self.name = 'No name'

    def adjust(self, transactions):
        self.transactions = transactions
        self.assets = FinAdjuster.compute_assets(transactions)
        self.create_data_structures()
        lenders = list(self.lenders)
        borrowers = list(self.borrowers)
        self.do_adjustments()
        return self.adjusted_transactions, lenders, borrowers

    def do_adjustments(self):
        self.adjusted_transactions = []
        while self.lenders:
            self.filter_equals()
            if not self.lenders:
                break

            borrowed_index, lent_index  = self.get_next_pair()
            if self.lenders[lent_index][0] == self.borrowers[borrowed_index]:
                self.eliminate_both(borrowed_index, lent_index)
            else:
                self.eliminate_one(borrowed_index, lent_index)

    def eliminate_both(self, borrowed_index, lent_index):
        self.adjusted_transactions.append((self.borrowers[borrowed_index][1], self.lenders[lent_index][1], self.borrowers[borrowed_index][0]))

    def eliminate_one(self, borrowed_index, lent_index):
        if self.lenders[lent_index][0] < self.borrowers[borrowed_index]:
            self.eliminate_lender(borrowed_index, lent_index)
        else:
            self.eliminate_borrower(borrowed_index, lent_index)

    def eliminate_lender(self, borrowed_index, lent_index):
        self.adjusted_transactions.append(
            (self.borrowers[borrowed_index][1], self.lenders[lent_index][1], self.lenders[lent_index][0]))
        self.remove(self.renders, lent_index)
    @abstractmethod
    def create_data_structures(self):
        pass

    @abstractmethod
    def filter_equals(self):
        pass

class MaxFinAdjuster(FinAdjuster):
    def __init__(self):
        super().__init__()
        self.name = 'Adjust between Max Lender and Max Borrower'

    def create_data_structures(self):
        # Define borrowers and lenders as sorted lists.
        self.lenders = []
        self.borrowers = []
        for person, asset in self.assets.items():
            if asset < 0:
                self.borrowers.append((-asset, person))
            elif asset > 0:
                self.lenders.append((asset, person))
        self.borrowers.sort(reverse=True)
        self.lenders.sort(reverse=True)

    def do_adjustments(self):
        self.adjusted_transactions = []
        while self.lenders:
            self.filter_equals()
            if not self.lenders:
                break

            lent_money, lender = self.lenders[0]
            borrowed_money, borrower = self.borrowers[0]
            self.borrowers = self.borrowers[1:]
            self.lenders = self.lenders[1:]

            if borrowed_money < lent_money:
                amount = borrowed_money
                self.insert_into_desc_list(self.lenders, lent_money - borrowed_money, lender)
            elif lent_money < borrowed_money:
                amount = lent_money
                self.insert_into_desc_list(self.borrowers, borrowed_money - lent_money, borrower)
            else:
                amount = borrowed_money
            self.adjusted_transactions.append((borrower, lender, amount))


    def filter_equals(self):
        pass



class MaxFinAdjusterWithEqualCheck(MaxFinAdjuster):
    def __init__(self):
        super().__init__()
        self.name = 'Adjust between Max Lender and Max Borrower, filter equal'

    def filter_equals(self):
        new_lenders = []
        new_borrowers = []
        borr_index = 0
        lend_index = 0
        while borr_index < len(self.borrowers) and lend_index < len(self.lenders):
            if self.borrowers[borr_index][0] == self.lenders[lend_index][0]:
                self.adjusted_transactions.append((self.borrowers[borr_index][1], self.lenders[lend_index][1], self.borrowers[borr_index][0]))
                borr_index += 1
                lend_index += 1

            if lend_index < len(self.lenders):
                while borr_index < len(self.borrowers) and self.borrowers[borr_index][0] > self.lenders[lend_index][0]:
                    new_borrowers.append(self.borrowers[borr_index])
                    borr_index += 1

            if borr_index < len(self.borrowers):
                while lend_index < len(self.lenders) and self.lenders[lend_index][0] > self.borrowers[borr_index][0]:
                    new_lenders.append(self.lenders[lend_index])
                    lend_index += 1

        while borr_index < len(self.borrowers):
            new_borrowers.append(self.borrowers[borr_index])
            borr_index += 1
        while lend_index < len(self.lenders):
            new_lenders.append(self.lenders[lend_index])
            lend_index += 1

        self.borrowers = new_borrowers
        self.lenders = new_lenders

class MinFinAdjuster(FinAdjuster):
    def __init__(self):
        super().__init__()
        self.name = 'Adjust between Min Lender and Min Borrower'

    def create_data_structures(self):
        # Define borrowers and lenders as sorted lists.
        self.lenders = []
        self.borrowers = []
        for person, asset in self.assets.items():
            if asset < 0:
                self.borrowers.append((-asset, person))
            elif asset > 0:
                self.lenders.append((asset, person))
        self.borrowers.sort()
        self.lenders.sort()

    def do_adjustments(self):
        self.adjusted_transactions = []
        while self.lenders:
            self.filter_equals()
            if not self.lenders:
                break

            lent_money, lender = self.lenders[0]
            borrowed_money, borrower = self.borrowers[0]
            self.borrowers = self.borrowers[1:]
            self.lenders = self.lenders[1:]

            if borrowed_money < lent_money:
                amount = borrowed_money
                self.insert_into_asc_list(self.lenders, lent_money - borrowed_money, lender)
            elif lent_money < borrowed_money:
                amount = lent_money
                self.insert_into_asc_list(self.borrowers, borrowed_money - lent_money, borrower)
            else:
                amount = borrowed_money
            self.adjusted_transactions.append((borrower, lender, amount))


    def filter_equals(self):
        pass

class MinFinAdjusterWithEqualCheck(MinFinAdjuster):
    def __init__(self):
        super().__init__()
        self.name = 'Adjust between Min Lender and Min Borrower, filter equal'

    def filter_equals(self):
        new_lenders = []
        new_borrowers = []
        borr_index = 0
        lend_index = 0
        while borr_index < len(self.borrowers) and lend_index < len(self.lenders):
            if self.borrowers[borr_index][0] == self.lenders[lend_index][0]:
                self.adjusted_transactions.append((self.borrowers[borr_index][1], self.lenders[lend_index][1], self.borrowers[borr_index][0]))
                borr_index += 1
                lend_index += 1

            if lend_index < len(self.lenders):
                while borr_index < len(self.borrowers) and self.borrowers[borr_index][0] < self.lenders[lend_index][0]:
                    new_borrowers.append(self.borrowers[borr_index])
                    borr_index += 1

            if borr_index < len(self.borrowers):
                while lend_index < len(self.lenders) and self.lenders[lend_index][0] < self.borrowers[borr_index][0]:
                    new_lenders.append(self.lenders[lend_index])
                    lend_index += 1

        while borr_index < len(self.borrowers):
            new_borrowers.append(self.borrowers[borr_index])
            borr_index += 1
        while lend_index < len(self.lenders):
            new_lenders.append(self.lenders[lend_index])
            lend_index += 1

        self.borrowers = new_borrowers
        self.lenders = new_lenders

class SimpleFinAdjuster(FinAdjuster):
    def __init__(self):
        super().__init__()
        self.name = 'Simple Adjuster'

    def create_data_structures(self):
        # Define borrowers and lenders as sorted lists.
        self.lenders = []
        self.borrowers = []
        for person, asset in self.assets.items():
            if asset < 0:
                self.borrowers.append((-asset, person))
            elif asset > 0:
                self.lenders.append((asset, person))

    def do_adjustments(self):
        self.adjusted_transactions = []
        while self.lenders:
            self.filter_equals()
            if not self.lenders:
                break

            lent_money, lender = self.lenders[0]
            borrowed_money, borrower = self.borrowers[0]
            self.borrowers = self.borrowers[1:]
            self.lenders = self.lenders[1:]

            if borrowed_money < lent_money:
                amount = borrowed_money
                self.lenders.append((lent_money - borrowed_money, lender))
            elif lent_money < borrowed_money:
                amount = lent_money
                self.borrowers.append((borrowed_money - lent_money, borrower))
            else:
                amount = borrowed_money
            self.adjusted_transactions.append((borrower, lender, amount))


    def filter_equals(self):
        pass


class Simulator:
    def __init__(self):
        self.minimum_counts = None
        self.combo_map = None
        self.case_listed = False
        self.one_cases = None
        self.two_cases = None

    def simulate_one(self, adjusters, n_people):
        # Generate transactions.
        transactions = self.generate_transactions(n_people)

        results = []
        minimum = n_people
        for adjuster in adjusters:
            adjusted_transactions, lenders, borrowers = adjuster.adjust(transactions)
            results.append((adjuster, len(transactions), len(adjusted_transactions)))
            if len(adjusted_transactions) < minimum:
                minimum = len(adjusted_transactions)
                minimum_transactions = adjusted_transactions
                minimum_lenders = lenders
                minimum_borrowers = borrowers

        index = 0
        mask = 1
        total = 0
        for result in results:
            if result[2] == minimum:
                self.minimum_counts[index] += 1
                total += mask
            mask <<= 1

            index += 1
        self.combo_map[total] = self.combo_map.get(total, 0) + 1
        return results

    def simulate(self):
        n_simulations = 1000
        n_people = 50
        # adjusters = [SimpleFinAdjuster(), MaxFinAdjuster(), MaxFinAdjusterWithEqualCheck(), MinFinAdjuster(), MinFinAdjusterWithEqualCheck()]
        adjusters = [MaxFinAdjuster(), MaxFinAdjusterWithEqualCheck()]
        results = []
        self.minimum_counts = [0] * len(adjusters)
        self.combo_map = dict()

        for i in range(n_simulations):
            results.append(self.simulate_one(adjusters, n_people))

        # Analysis
        adjuster_map = dict()
        for result in results:
            for each_result in result:
                # Each element is statistics about each adjuster
                (adjuster, n_transactions, n_adj_transactions) = each_result
                adj_data = adjuster_map.get(adjuster, [0, 0, 0, 0.0, 0])
                adj_data[0] += n_transactions
                adj_data[1] += n_people
                adj_data[2] += n_adj_transactions
                adj_data[3] += n_adj_transactions / (n_people - 1)
                adj_data[4] += 1
                adjuster_map[adjuster] = adj_data

        for adjuster, data in adjuster_map.items():
            print('Alg = %-60s, Average Transactions = %5d, Average People = %4d, Average adjusted transactions = %10.4f' % (adjuster.name, data[0] / n_simulations, data[1] / n_simulations, data[2] / n_simulations))

        print(self.minimum_counts)
        for combo in sorted(self.combo_map.keys()):
            value = self.combo_map[combo]
            algs = ''
            mask = 1
            for i in range(len(adjusters)):
                if (combo & mask) != 0:
                    algs += '%d ' % (i+1)
                mask <<= 1
            print ('%-15s %5d' % (algs, value))
        print(self.combo_map)

    def generate_transactions(self, n_people):
        r = random.Random()
        a = -100
        b = 100
        transactions = []
        for borrower in range(n_people):
            for lender in range(n_people):
                if borrower != lender:
                    # Generate an amount between 0 and 199.
                    v = r.randint(a, b)
                    if v < 0:
                        transactions.append(('%d' % borrower, '%d' % lender, -v))
                    elif v > 0:
                        transactions.append(('%d' % lender, '%d' % borrower, v))
        return transactions

def basic_test():
    transactions = [
        ('A', 'B', 10),
        ('B', 'C', 3),
        ('B', 'D', 7),
        ('E', 'A', 30),
        ('C', 'E', 15),
        ('F', 'A', 3),
        ('A', 'C', 7),
        ('D', 'F', 9),
        ('F', 'E', 1)
    ]
    adj = MaxFinAdjuster(transactions)
    # result = adjust(transactions)
    result = adj.adjust()
    print('\n Final transactions:')
    for t in result:
        print('    %s to %s: %3d' % (t[0], t[1], t[2]))


if __name__ == '__main__':
    # basic_test()
    s = Simulator()
    s.simulate()

