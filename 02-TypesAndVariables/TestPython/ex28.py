height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
bmi = float(weight)/(float(height)/100)**2
print(bmi)

if float(bmi) >= 18.5 and float(bmi) <= 25:
    print('Correct weight: True')
else:
    print('Correct weight: False')