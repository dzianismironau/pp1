def f(password):
    result = True
    new_word = password
    if len(password) < 6:
        result = False
    else:
        for i in new_word:
            if result == False:
                break
            password = password[1:]
            for j in password:
                if i == j:
                    result = False
                    break
                else:
                    result = True
    return result

if __name__ == '__main__':
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))