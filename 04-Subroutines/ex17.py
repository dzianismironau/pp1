def different(n1, n2, n3):
    if n1 == n2 and n1 == n3 and n2 == n3:
        return False
    else:
        return True

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))

if different(first_number, second_number, third_number):
    print(f'Numbers {first_number}, {second_number} and {third_number} are different')
else: 
    print('They are the same')