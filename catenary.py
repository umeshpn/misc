import math


class Catenary:
    def __init__(self):
        self.a = 35.0 / 3
        self.DELTA = 0.1

    def draw_full(self):
        x = 0.0
        y = 0.0
        while x <= 22.7:
            last_x = x
            last_y = y
            x += self.DELTA
            y = self.a * math.cosh(x/self.a) - self.a
            print('draw (%10.4f, %10.4f)  -- (%10.4f, %10.4f)' % (last_x, last_y, x, y))
            print('draw (%10.4f, %10.4f)  -- (%10.4f, %10.4f)' % (-last_x, last_y, -x, y))

    def draw(self):
        x = 0.0
        y = 0.0
        print ('\\draw(%10.4f, %10.4f)' % (x, y))
        while x <= 22.7:
            x += self.DELTA
            y = self.a * math.cosh(x/self.a) - self.a
            # print('%10.4f %10.4f' % (x, y))
            print('    -- (%10.4f, %10.4f)' % (x, y))
        print(';')


if __name__ == '__main__':
    c = Catenary()
    c.draw_full()
    c.draw()
