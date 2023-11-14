def f(card_number):
    unvisible_number = ''
    if len(card_number) == 16:
        unvisible_number = card_number[:2] + '*'*10 + card_number[12:]
    else:
        unvisible_number = 'Wrong number, enter 16 digits'
    return unvisible_number

if __name__ == '__main__':
    print(f('5290312400019022'))