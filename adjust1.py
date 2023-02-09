def create_arrays(assets):
    lender_array = []  # In the order of assets, from big to small
    borrower_array = []  # In the order of debt, from big to small.
    for key, value in assets.items():
        if value > 0:
            lender_array.append((key, value))  # PriorityQueue requires first value of tuple the key.
        if value < 0:
            borrower_array.append((key, -value))
        # We ignore all elaments with zero asset.
        lender_array.sort(key=lambda x:-x[1])
        borrower_array.sort(key=lambda x:-x[1])

    return lender_array, borrower_array

def compute_assets(transactions):
    assets = dict()  # person -> overall money.  +: asset, -: debt
    for t in transactions:
        (from_person, to_person, amount) = t
        assets[from_person] = assets.get(from_person, 0) - amount
        assets[to_person] = assets.get(to_person, 0) + amount
    return assets

def do_adjustments(lender_array, borrower_array):
    adjustments = []
    # We iterate until all lenders get all their money.
    while not lender_array.empty():
        next = next_equal_amounts(lender_array, borrower_array, 0, 0)
        while next:
            adjustments.append((lender_array[], largest_lender, largest_lent_amount))


def adjust(transactions):
    """
    :param transactions: Each transaction is (from_person, to_person, amount)
    :return: adjustments: Each adjustment is (from_person, to_person, amount)
    """

    # Find the assets of each person.
    assets = compute_assets(transactions)
    lender_array, borrower_array = create_arrays(assets)
    adjustments = do_adjustments(lender_array, borrower_array)

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

    result = adjust(transactions)

    print('\n Final transactions:')
    for t in result:
        print('    %s to %s: %3d' % (t[0], t[1], t[2]))

