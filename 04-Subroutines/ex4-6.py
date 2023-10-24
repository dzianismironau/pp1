def computepay(hours, rate):
    over_time = 0
    if hours > 40:
        over_time = hours - 40
    return (hours - over_time)*rate + over_time * rate *1.5

work_time = int(input('Enter Hours: '))
work_rate = int(input('Enter Rate: '))
print(f'Pay: {computepay(work_time, work_rate)}')