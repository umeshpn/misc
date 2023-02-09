from queue import PriorityQueue

debug = False

class TransactionAdjuster:

    def adjust(self, transactions):
        """
        :param transactions: Each transaction is (from_person, to_person, amount)
        :return: adjustments: Each ajustment is (from_person, to_person, amount)
        """

        # Find the assets of each person.
        assets = self.compute_assets(transactions)

        rich_heap = PriorityQueue() # In the order of assets, from big to small
        poor_heap = PriorityQueue() # In the order of debt, from big to small.

        for key, value in assets.items():
            if value > 0:
                rich_heap.put((-value, key, value))  # PriorityQueue requires first value of tuple the key.
            if value < 0:
                poor_heap.put((value, key, -value))
            # We ignore all elaments with zero asset.


        adjustments = []
        while not rich_heap.empty():
            (key, richest_name, richest_asset) = rich_heap.get()
            (key, poorest_name, poorest_debt) = poor_heap.get()
            amount = poorest_debt if poorest_debt < richest_asset else richest_asset
            adjustments.append((poorest_name, richest_name, amount))
            remaining_debt = poorest_debt - amount
            if remaining_debt > 0:
                poor_heap.put((-remaining_debt, poorest_name, remaining_debt))

            remaining_asset = richest_asset - amount
            if remaining_asset > 0:
                rich_heap.put((-remaining_asset, richest_name, remaining_asset))

        return adjustments

    def compute_assets(self, transactions):
        assets = dict()  # person -> overall money.  +: asset, -: debt
        for t in transactions:
            (from_person, to_person, amount) = t
            assets[from_person] = assets.get(from_person, 0) - amount
            assets[to_person] = assets.get(to_person, 0) + amount
        return assets

    def adjust2(self, transactions):
        """
        :param transactions: Each transaction is (from_person, to_person, amount)
        :return: adjustments: Each ajustment is (from_person, to_person, amount)
        """

        print('Transactions:')
        for t in transactions:
            print('    %s to %s: %3d' % (t[0], t[1], t[2]))

        assets = self.compute_assets(transactions)

        rich_heap = PriorityQueue()
        poor_heap = PriorityQueue()

        for key, value in assets.items():
            if value > 0:
                rich_heap.put((-value, key, value))
            if value < 0:
                poor_heap.put((value, key, -value))
            # We ignore all elaments with zero asset.


        adjustments = []
        while not rich_heap.empty():
            self.print_heap("rich_heap", rich_heap)
            self.print_heap("poor_heap", poor_heap)
            (key, richest_name, richest_asset) = rich_heap.get()
            (key, poorest_name, poorest_debt) = poor_heap.get()
            amount = poorest_debt if poorest_debt < richest_asset else richest_asset

            print('%s to %s: %d' % (poorest_name, richest_name, amount))
            adjustments.append((poorest_name, richest_name, amount))
            remaining_debt = poorest_debt - amount
            if remaining_debt > 0:
                poor_heap.put((-remaining_debt, poorest_name, remaining_debt))

            remaining_asset = richest_asset - amount
            if remaining_asset > 0:
                rich_heap.put((-remaining_asset, richest_name, remaining_asset))

        return adjustments

    def print_heap(self, name, heap):

        q = PriorityQueue(heap);
        print('%s = [' % name, end='')
        for elem in heap.queue:
            print(' (%s, %d) ' % (elem[1], elem[2]), end='')
        print(']')


    def adjust1(self, transactions):
        """
        :param transactions: Each transaction is (from_person, to_person, amount)
        :return: adjustments: Each ajustment is (from_person, to_person, amount)
        """

        print('Transactions:')
        for t in transactions:
            print('    %s to %s: %3d' % (t[0], t[1], t[2]))

        # Find the assets of each person.  Also, count how many transactions each has.
        assets = dict()  # person -> overall money.  +: asset, -: debt
        actions = dict() # Person -> # of transactions
        for t in transactions:
            (from_person, to_person, amount) = t
            assets[from_person] = assets.get(from_person, 0) - amount
            assets[to_person] = assets.get(to_person, 0) + amount
            actions[from_person] = actions.get(from_person, 0) + 1
            actions[to_person] = actions.get(to_person, 0) + 1

        if debug:
            print(assets)

        # We can eliminate all people who have zero assets.
        assets = {key: value for key, value in assets.items() if value != 0}
        if debug:
            print(assets)

        rich = sorted([key for key, value in assets.items() if value > 0], key=lambda x:-assets[x])
        poor = sorted([key for key, value in assets.items() if value < 0], key=lambda x:assets[x])

        print('People who need to get money:')
        for r in rich:
            print('    %-4s %3d' % (r, assets[r]))

        print('People who owe money:')
        for p in poor:
            print('    %-4s %3d' % (p, -assets[p]))


        if debug:
            print('rich = {}', rich)
            print('poor = {}', poor)

        adjustments = []
        while rich and poor:
            if debug:
                print('assets = ', assets)
            max_debt = assets[poor[0]]
            max_credit = assets[rich[0]]
            if -max_debt >= max_credit:
                if debug:
                    print('%s gives %d to %s' % (poor[0], max_credit, rich[0]))
                transaction = (poor[0], rich[0], max_credit)
                assets[poor[0]] += max_credit
                assets[rich[0]] = 0
                rich = rich[1:]

            else:
                if debug:
                    print('%s gives %d to %s' % (poor[0], -max_debt, rich[0]))
                transaction = (poor[0], rich[0], -max_debt)
                assets[rich[0]] += max_debt
                assets[poor[0]] = 0
                poor = poor[1:]
            if debug:
                rich.sort(key=lambda x:-assets[x])
                poor.sort(key=lambda x:assets[x])
                print('rich = {}', rich)
                print('poor = {}', poor)

            adjustments.append(transaction)

        if debug:
            print('rich = {}', rich)
            print('poor = {}', poor)
            print('adjustments = {}', adjustments)
            print('assets = {}', assets)
        return adjustments

if __name__ == '__main__':
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

    adj = TransactionAdjuster()
    result = adj.adjust(transactions)

    print('\n Final transactions:')
    for t in result:
        print('    %s to %s: %3d' % (t[0], t[1], t[2]))


