import myrange

start = 2
end = 15
number = int(input('Enter a number: '))
print(f'Number {number} un the range <{start}, {end}>: {myrange.is_in_range(start,end,number)}')