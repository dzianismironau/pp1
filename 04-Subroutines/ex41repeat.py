def f(n):
    result = 2
    now = result
    while n > 1:
        now += 1
        is_prime = True
        for i in range(2,now):
            if now%i == 0:
                is_prime = False
        if is_prime == True:
            result = now
            n -= 1
    return result

if __name__ == '__main__':
    print(f(1))
    print(f(5))