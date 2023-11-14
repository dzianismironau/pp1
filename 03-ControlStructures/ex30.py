time_12 = ''
while True:
    time_24 = input('Enter time (24-hour format): ')

    if time_24[1] == ':' or time_24[2] == ':':
        break
    else:
        print('Try one more time!')

if len(time_24) != 5 or int(time_24[0:2]) < 12:
    print(f'Time in 12-hour format: {time_24 + 'am'}')
elif int(time_24[0:2]) >= 12:
    time_12 = str(int(time_24[0:2]) - 12) + ':' + time_24[3:5] + 'pm'
    print(f'Time in 12-hour format: {time_12}')
