number = int(input('Enter number: '))
result = 0
for i in range(1,11):
    result = number * i 
    print(f'{number} x {i} = {result}')
    i += 1
