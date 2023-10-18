fathIncome = input("Enter father's income: ")
mothIncome = input("Enter mother's income: ")
numPeople = input("Enter number of people in family: ")

totalIncome = int(fathIncome) + int(mothIncome)
incPerPerson = int(totalIncome) / int(numPeople)

print(f'Income per person: {incPerPerson}')