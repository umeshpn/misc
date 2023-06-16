
def f2cf(num: int, den: int) -> []:
    return [den] if num == 1 else [(den // num)] + f2cf(den % num, num)


if __name__ == '__main__':
    print(f2cf(98, 199))