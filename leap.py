
def is_leap1(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def is_leap(year):
    if year % 4 != 0:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return True


if __name__ == '__main__':
    assert (is_leap(1885) == False)
    assert (is_leap(1960) == True)
    assert (is_leap(1900) == False)
    assert (is_leap(2000) == True)

