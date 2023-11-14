amount = int(input('Enter the amount in PLN: '))
zl_5 = amount//5
zl_2 = (amount - zl_5*5)//2
zl_1 = (amount - zl_5*5 - zl_2*2)//1

print(f'The amount of PLN {amount} in coins:\n5 zł - {zl_5}\n2 zł - {zl_2}\n1 zł - {zl_1}')