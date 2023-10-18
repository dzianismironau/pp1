cardNumber = input('Enter credit card number: ')
rightNumber = cardNumber[:4] + ' ' + cardNumber[4:8] + ' ' + cardNumber[8:12] + ' ' + cardNumber[12:]
if len(cardNumber) > 16 or len(cardNumber) < 16:
    print('Wrong number')
else:
    print(f'Card number: {rightNumber}')
