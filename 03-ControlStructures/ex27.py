fb = input('Do you use facebook? (Yes/No): ')
tw = input('Do you use twitter? (Yes/No): ')
inst = input('Do you use twitter? (Yes/No): ')

if fb and tw == 'Yes' or fb and tw == 'yes' or fb and inst == 'Yes' or fb and inst == 'yes' or tw and inst == 'Yes' or tw and inst == 'yes':
    print('A person can be a good influencer!')
else:
    print('Try one more time')