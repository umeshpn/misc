
def compute_gain2(interest):
    """Given an annual interest rate, compute the gain for the particular problem."""
    alpha = 1 + interest
    c = 20000 * (alpha ** 15 + alpha ** 10)
    p = 8618 * (alpha ** 21 - alpha ** 11) / interest
    return c + 65000 - p

def compute_gain1(interest):
    """Given an annual interest rate, compute the gain for the particular problem."""
    alpha = 1 + interest
    c = 15000 * (alpha ** 7 + alpha ** 3)
    p = 1200 * (alpha ** 16 - alpha) / interest
    return c + 20000 - p

def compute_gain(interest):
    """Given an annual interest rate, compute the gain for the particular problem."""
    alpha = 1 + interest
    p = 37676 * (alpha ** 21 - alpha ** 9) / interest
    return 1684000 - p

def print_gains():
    "Prints gains for various interest rates."
    for i in range(1, 11):
        print('%d \\%% & %10.2f\\\\' % (i, (compute_gain(i * 0.01))))  # LaTeX table row.

def get_effective_rate(low, high):
    """Use bisection to pinpoint the effective rate"""
    while True:
        mid = 0.5 * (low + high)
        gain = compute_gain(mid)
        print("%f %f %f %f" % (low, high, mid, gain))

        if abs(gain) < 0.001:
            break
        elif gain > 0:
            low = mid
        else:
            high = mid

if __name__ == '__main__':
    print_gains()
    # get_effective_rate(0.09, 0.10)
