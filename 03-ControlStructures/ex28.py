num = str(input('Enter EAN-13 article number: '))

if len(num) == 13 and num[0:3] == '590':
    print('Article number is correct\nArticle manufactured in Poland')
elif len(num) == 13:
    print('Article number is correct')
else:
    print('Wrong number')
