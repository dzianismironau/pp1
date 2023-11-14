def f(card_number):
    masked_number = card_number[:2] + '*'*10 + card_number[-4:]
    return masked_number

if __name__ == '__main__':
    print(f("5288888888889022"))