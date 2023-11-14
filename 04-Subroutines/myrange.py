def is_in_range(x, y, number):
    if x <= number <= y:
        return True
    else:
        return False
    
if __name__ == '__main__':
    start = 2
    end = 15
    number = int(input('Enter a number: '))
    print(f'Number {number} un the range <{start}, {end}>: {is_in_range(start,end,number)}')