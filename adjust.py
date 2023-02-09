from queue import PriorityQueue
import random

def compute_assets(transactions):
    assets = dict()  # person -> overall money.  +: asset, -: debt
    for t in transactions:
        (from_person, to_person, amount) = t
        assets[from_person] = assets.get(from_person, 0) - amount
        assets[to_person] = assets.get(to_person, 0) + amount
    return assets

def create_heaps(assets):
    lender_heap = PriorityQueue()  # In the order of assets, from big to small
    borrower_heap = PriorityQueue()  # In the order of debt, from big to small.
    for key, value in assets.items():
        if value > 0:
            lender_heap.put((-value, key, value))  # PriorityQueue requires first value of tuple the key.
        if value < 0:
            borrower_heap.put((value, key, -value))
        # We ignore all elaments with zero asset.
    return lender_heap, borrower_heap


def do_adjustments(lender_heap, borrower_heap):
    adjustments = []
    # We iterate until all lenders get all their money.
    while not lender_heap.empty():

        # Get the largest lender.
        (key, largest_lender, largest_lent_amount) = lender_heap.get()

        # Get the largest borrower.
        (key, largest_borrower, largest_borrowed_amount) = borrower_heap.get()

        if largest_lent_amount > largest_borrowed_amount:
            adjustments.append((largest_borrower, largest_lender, largest_borrowed_amount))
            remaining_lent_amount = largest_lent_amount - largest_borrowed_amount
            lender_heap.put((-remaining_lent_amount, largest_lender, remaining_lent_amount))

        elif largest_lent_amount < largest_borrowed_amount:
            adjustments.append((largest_borrower, largest_lender, largest_lent_amount))
            remaining_borrowed_amount = largest_borrowed_amount - largest_lent_amount
            borrower_heap.put((-remaining_borrowed_amount, largest_borrower, remaining_borrowed_amount))

        else:  # Equal amount
            adjustments.append((largest_borrower, largest_lender, largest_lent_amount))

        # # Settle either the largest lender or the largest borrower, whoever has the lesser amount.
        # amount = largest_borrowed_amount if largest_borrowed_amount < largest_lent_amount else largest_lent_amount
        #
        # # Make the borrower pay the amount to the lender.
        # adjustments.append((largest_borrower, largest_lender, amount))
        #
        # # If the borrower still has debt, put him back to the heap with the new debt.
        # remaining_debt = largest_borrowed_amount - amount
        # if remaining_debt > 0:
        #     borrower_heap.put((-remaining_debt, largest_borrower, remaining_debt))
        #
        # # If the lender still has lent money, put him back to the heap with the new amount.
        # remaining_lent_amount = largest_lent_amount - amount
        # if remaining_lent_amount > 0:
        #     lender_heap.put((-remaining_lent_amount, largest_lender, remaining_lent_amount))
    return adjustments

def adjust(transactions):
    """
    :param transactions: Each transaction is (from_person, to_person, amount)
    :return: adjustments: Each adjustment is (from_person, to_person, amount)
    """

    # Find the assets of each person.
    assets = compute_assets(transactions)
    lender_heap, borrower_heap = create_heaps(assets)
    adjustments = do_adjustments(lender_heap, borrower_heap)

    return adjustments

def adjust1(transactions):
    assets = compute_assets(transactions)

    # Create lists.
    lender_list = []
    borrower_list = []
    for key, value in assets.items():
        if value > 0:
            lender_list.append((key, value))
        if value < 0:
            borrower_list.append((key, -value))

    adjustments = []
    while lender_list:

        # Remove the first elements
        lender = lender_list[0]
        borrower = borrower_list[0]
        borrower_list = borrower_list[1:]
        lender_list = lender_list[1:]

        if lender[1] > borrower[1]:
            adjustments.append((borrower[0], lender[0], borrower[1]))
            lender_list.append((lender[0], lender[1] - borrower[1]))
        elif lender[1] < borrower[1]:
            adjustments.append((borrower[0], lender[0], lender[1]))
            borrower_list.append((lender[0], borrower[1] - lender[1]))
        else:  # Amounts are the same.
            adjustments.append((borrower[0], lender[0], lender[1]))

    return adjustments

def generate_one_case(count0, count1):
    r = random.Random()
    n_people = 50
    a = -100
    b = 100
    transactions = []
    for borrower in range(n_people):
        for lender in range(n_people):
            # Generate an amount between 0 and 199.
            v = r.randint(a, b)
            if v < 0:
                transactions.append(('%d' % borrower, '%d' % lender, -v))
            elif v > 0:
                transactions.append(('%d' % lender, '%d' % borrower, v))

    # print(transactions)
    # print('Input: %d' % len(transactions))
    result = adjust(transactions)
    result1 = adjust1(transactions)
    count0.append(len(result))
    count1.append(len(result1))
    # print('Result 1:', result)
    # print('Result 2:', result1)
    # print('Alg 1: %d' % len(result))
    # print('Alg 2: %d' % len(result1))

if __name__ == '__main__':
    count0 = []
    count1 = []
    n = 100
    for i in range(n):
        generate_one_case(count0, count1)
    print(count0)
    print(count1)
    average0 = sum(count0) / len(count0)
    average1 = sum(count1) / len(count1)
    print(len(average0, average1)
    print(average1)
    # transactions = [
    #     ('A', 'B', 10),
    #     ('B', 'C', 3),
    #     ('B', 'D', 7),
    #     ('E', 'A', 30),
    #     ('C', 'E', 15),
    #     ('F', 'A', 3),
    #     ('A', 'C', 7),
    #     ('D', 'F', 9),
    #     ('F', 'E', 1)
    # ]
    #
    # # result = adjust(transactions)
    # result = adjust1(transactions)
    #
    # print('\n Final transactions:')
    # for t in result:
    #     print('    %s to %s: %3d' % (t[0], t[1], t[2]))


