cur_price = float(input('Enter current price: '))
prev_price = float(input('Enter previous price: '))
sale = int((prev_price-cur_price)/prev_price*100)
if sale >= 10:
    print(f'Buy the product!!\nProduct price reduced by {sale}%')
else:
    print('So little sale((')