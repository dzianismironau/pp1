def f(number,even):
    k = 0
    if even == True:
        for i in str(number):
            if int(i)%2 == 0:
                k += int(i)
    else:
        for j in str(number):
            if int(j)%2 != 0:
                k += int(j)
    return k

if __name__ == '__main__':
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))

