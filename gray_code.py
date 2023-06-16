class GrayCodeGenerator:

    @staticmethod
    def reverse_gray(x):
        y = []
        if len(x) == 0:
            return y

        y.append(x[0])
        last_y = y[0]
        for x_value in x[1:]:
            y.append((1 - x_value) * last_y + (1 - last_y) * x_value)
            # y.append(x_value + last_y - 2 * x_value * last_y)
        return y


if __name__ == '__main__':
    x_array = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [0, 1, 0],
        [1, 1, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]

    for x in x_array:
        y = GrayCodeGenerator.reverse_gray(x)
        print('%s => %s' % (x, y))
