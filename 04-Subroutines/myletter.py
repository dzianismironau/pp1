def e_calculate(text):
    k = 0
    for i in text:
        if i == 'e' or i == 'E':
            k += 1
    return k

if __name__ == '__main__':
    print(e_calculate('eeeee'))
