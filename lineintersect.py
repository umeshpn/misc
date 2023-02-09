
class LineIntersector:
    def point_of_intersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        a = x1 * y2 - y1 * x2
        b = x3 * y4 - y3 * x4
        x34 = x3 - x4
        x12 = x1 - x2
        y34 = y3 - y4
        y12 = y1 - y2

        x = (a * x34 - x12 * b) / (x12 * y34 - y12 * x34)
        y = (a * y34 - y12 * b) / (x12 * y34 - y12 * x34)

        return x, y

    def print_poi(self, x1, y1, x2, y2, x3, y3, x4, y4):
        print('Line 1 : (%f, %f) -- (%f, %f)' % (x1, y1, x2, y2))
        print('Line 2 : (%f, %f) -- (%f, %f)' % (x3, y3, x4, y4))
        x, y = self.point_of_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
        print('Intersection: (%f, %f)\n' % (x, y))

if __name__ == '__main__':
    li = LineIntersector()
    li.print_poi(0, 5, 1, 0, 0, 2.5, 1.5, 2.5)
    li.print_poi(0, 5, 2, 0, 0, 2.5, 1.5, 2.5)

    li.print_poi(0, 5, 1, 0, 0, 0, 1.5, 2.5)
    li.print_poi(0, 5, 2, 0, 0, 0, 1.5, 2.5)
