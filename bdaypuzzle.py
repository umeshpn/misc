
def main():
    n = 1
    p = 1.0

    while n < 100:
        n += 1
        mult = 365.0 / (366.0 - n)
        p *= mult
        print('$%2d$ & $%12.8f$ & $%12.8f$ & \\\\' % (n, mult, p))

if __name__ == '__main__':
    main()