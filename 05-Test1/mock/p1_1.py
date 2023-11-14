def f(amount_to_pay):
    coin_5 = amount_to_pay//5
    coin_2 = (amount_to_pay - coin_5*5)//2
    coin_1 = amount_to_pay - (coin_5*5 + coin_2*2)
    return (coin_1 + coin_2 + coin_5)

if __name__ == '__main__':
    print(f(23))
    print(f(8))
