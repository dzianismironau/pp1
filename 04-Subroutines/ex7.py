bmi = lambda weight, height: weight/(height/100)**2

kg = int(input('Enter your weight in kg: '))
cm = int(input('Enter your height in cm: '))

print(bmi(kg, cm))