def numbers(n):
    k = ''
    for i in range(1, n+1):
        k += str(i) + ' '
    return (f"Numbers <1, {n}>: {k}")

your_num = int(input('Enter a number: '))
print(numbers(your_num))