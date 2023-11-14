bin_num = input('Enter binary number: ')
dec_num = 0
if len(bin_num) == 4:
    dec_num = int(bin_num[-1])*2**0 + int(bin_num[-2])*2**1 + int(bin_num[-3])*2**2 + int(bin_num[-4])*2**3
    print(f'Decimal notation: {dec_num}')
else:
    print('Wrong binary number!')