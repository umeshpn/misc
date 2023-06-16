import contfrac


def frac2cf(num, den):
    value = (num, den)
    coeff = list(contfrac.continued_fraction(value))
    print('cf = ', coeff)
    conv = list(contfrac.convergents(value))
    print('convergents = ', conv)


def cf2frac(coeff_list):
    f = contfrac.convergent(coeff_list, 100)
    print(f)


if __name__ == '__main__':
    # frac2cf(415, 93)
    cf2frac([4, 2, 6, 7])
    frac2cf(98, 199)
    cf2frac([0, 2, 32, 1, 2])
