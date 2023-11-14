a = int(input('Enter value of side A: '))
b = int(input('Enter value of side B: '))

for i in range(a):
    if i == 0 or i == a - 1:
        print(b * '*')
    else:
        print('*' + (b-2)*' ' + '*')