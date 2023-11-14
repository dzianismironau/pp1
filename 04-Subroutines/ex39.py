def f(sentence):
    word = ''
    arr = sentence.split(' ')
    for i in arr:
        word += i
    return f'"{word}"'

if __name__ == '__main__':
    print(f("integrated development environment"))