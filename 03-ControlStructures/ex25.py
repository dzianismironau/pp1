pr_num = float(input('Enter number of products: '))
pr_price = float(input('Enter product price: '))
full_price = 0
if pr_num <= 2 and pr_num > 0:
    full_price = pr_num*pr_price
    print(f'Amount to pay: {round(full_price, 2)}')
elif pr_num > 2:
    full_price = pr_price*2 + (pr_num - 2)*(pr_price*0.75)
    print(f'Amount to pay: {round(full_price, 2)}')
else:
    print('Wrong number of products')
