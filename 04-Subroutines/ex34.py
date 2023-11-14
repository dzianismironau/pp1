def f(n):
    k = ''
    for i in range(1, n+1):
        k += str(i)
    return f'"{k}"'

if __name__ == '__main__':
    print(f(11))
    print(f(4))