def month(n):
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_name[n-1]

enter_number = int(input('Enter month name: '))
print(f'Month name: {month(enter_number)}')