

def dummy(start, difference, modulus, remainder):
    print("\nSolving %dx + %d and %dy + %d" % (difference, start, modulus, remainder))
    n = start
    i = 0
    while i < modulus:
        print(i+1, n, n % modulus)
        if n % modulus == remainder:
            print ('Answer = ', n)
        n += difference
        i += 1

if __name__ == '__main__':
    dummy(9, 23, 19, 7)
    dummy(216, 437, 17, 4)
    dummy(2401, 7429, 13, 3)
    dummy(91549, 96577, 7, 2)

    # for k in [7, 13, 17, 19, 23]:
    #     print(k, 299952 % k)


