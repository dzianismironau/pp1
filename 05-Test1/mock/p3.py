def f(name):
    acronim = ''
    words = name.split(' ')
    for i in words:
        acronim += i[0]
    return acronim

if __name__ == '__main__':
    print(f('Internet of Things'))
    print(f('For Your Information'))
    print(f('Python'))