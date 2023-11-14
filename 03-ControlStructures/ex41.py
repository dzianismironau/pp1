right_pin = 9421

for i in range(3):
    enter_pin = int(input('Enter the PIN code: '))
    if enter_pin == right_pin:
        print('Pass')
        break
    else:
        print('Incorrect...')
        i += 1
    
    if i == 3:
        print('Sorry, your payment card has been blocked')