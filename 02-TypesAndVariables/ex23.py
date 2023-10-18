a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter c: ')
s = (int(a)+int(b)+int(c))/2
area = (s*((s-int(a))*(s-int(b))*(s-int(c))))**(1/2)
circ = (int(a)+int(b)+int(c))
print(f'Triangle area: {area}\nTriangle circ: {circ}')
