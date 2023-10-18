number = input('Enter phone number: ')
newNumber = number[0:3] + '-' + number[3:6] + '-' + number[6:]
if len(number) > 9 or len(number) < 9:
    print('Wrong number')
else:
    print(f'Phone number {newNumber}')