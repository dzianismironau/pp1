sum = 0
iterations = 0

while True:
    num = int(input('Enter number: '))
    sum += num
    iterations += 1
    if num == 0:
        break

mean = sum/(iterations-1)

print(f'RESULT: Quantity={(iterations-1)}, Sum={sum}, Mean={int(mean)}')