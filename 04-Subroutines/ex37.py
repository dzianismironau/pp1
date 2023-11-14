def f(n):
    a = 1
    b = 0
    for i in range(n):
        a,b = b,a+b
    return a

if __name__ == '__main__':
    print(f(5))
    print(f(9))