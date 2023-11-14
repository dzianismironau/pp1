def f(text):
    separated_text = ''
    for i in text:
        separated_text += i + '-'
    return f'"{separated_text[:-1]}"'

if __name__ == '__main__':
    print(f('University'))
    print(f("UE"))
    print(f("x"))
    print(f(""))