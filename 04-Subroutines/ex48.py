def f(product_code):
    sum = 0
    for i in product_code[:-1]:
        sum += int(i)
    if sum%7 == int(product_code[-1]):
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))