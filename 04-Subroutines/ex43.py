def f(name):
    new_name = ''
    arr = name.split(' ')
    for i in arr:
        new_name += i[0]
    return f'"{new_name}"'

if __name__ == '__main__':
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))