def f(dice):
    result = ''
    max = 0
    for i in dice:
        row = 0
        for j in dice:
            if i == j:
                row += 1
        if row > max:
            result = i
            max = row
    return result

if __name__ == '__main__':
    print(f("5233165554211"))
    print(f('2133'))
