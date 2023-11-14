def f(amount_to_pay):
    coin_5 = amount_to_pay//5
    coin_2 = (amount_to_pay%5)//2
    coin_1 = (amount_to_pay%5%2)//1
    return coin_5 + coin_2 + coin_1

if __name__ == '__main__':
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))