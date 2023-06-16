
def solve_congr(a, b, c):
    """Solves ax + b = cy."""
    for x in range(c):
        b_c = (a * x + b) % c
        print(x, b_c)
        if b_c == 0:
            print(x)
            break

if __name__ == '__main__':
    solve_congr(221, 65, 195)