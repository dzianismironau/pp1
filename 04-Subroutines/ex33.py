def f(n):
    k = ''
    for i in range(n):
        k += '*/'
    return f'"{k[:-1]}"'

if __name__ == '__main__':
    print(f(4))
    print(f(1))