import math

class PiCalculator:
    def gauss_legendre(self):
        a = 1.0
        b = 1.0 / math.sqrt(2.0)
        t = 0.25
        p = 1.0
        for i in range(10):
            new_a = 0.5 * (a + b)
            new_b = math.sqrt(a * b)
            temp = a - new_a
            new_t = t - p * temp * temp
            new_p = 2 * p

            numer = new_a + new_b
            print(0.25 * numer * numer / new_t)

            a = new_a
            b = new_b
            t = new_t
            p = new_p

if __name__ == '__main__':
    PiCalculator().gauss_legendre()
