numbers = ''
for i in range(1,31):
        
        if i%3 == 0 and i%5 == 0:
            numbers += ' BINGO'
        elif i%3 == 0:
            numbers += ' THREE' 
        elif i%5 == 0:
            numbers += ' FIVE'
        else:
            numbers += ' ' + str(i)
            
        i += 1

print(numbers)