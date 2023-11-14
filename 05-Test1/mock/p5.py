def f(binary_number):
    for i in binary_number:
        if i != '1' and i != '0':
            return False
        else:
            continue
    return True

if __name__ == '__main__':   
    print(f('101101'))
    print(f('1311a10100'))
    print(f('1010101010101010101111000000'))