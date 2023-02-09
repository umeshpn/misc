import ewordle

if __name__ == '__main__':
    letters = input('letters: ')
    ws = ewordle.EWordle()
    print(letters)
    ws.print_non_candidates(letters)