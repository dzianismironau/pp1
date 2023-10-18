buy = input('Bank buys EUR: ')
sell = input('Bank sells EUR: ')
spread = float(sell) - float(buy)
print(f'Spread: {round(spread, 4)}')