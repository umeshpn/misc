# import math
from math import sqrt

# Quadratic equation.


def solve_quadratic(a, b, c):
    desc = b * b - 4 * a * c  # Comment
    ds = sqrt(desc)
    two_a = 2 * a
    x1 = (-b + ds) / two_a
    x2 = (-b - ds) / two_a

    return x1, x2


if __name__ == '__main__':
    x1, x2 = solve_quadratic(1, 10, 3)
    print('x1 = ', x1)
    print('x2 = ', x2)

    # hello("Vishakh");
    # hello("Kichu");
    # hello("Uma");



