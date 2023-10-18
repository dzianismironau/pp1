human_age = int(input("Enter dog's age in human years: "))
dog_age = 0
if human_age > 2:
    dog_age = 2*10.5 + (human_age-2)*4
    print(f"The dog's age in dog’s years is {int(dog_age)} years.")
elif human_age <= 2 and human_age > 0:
    dog_age = human_age*10.5
    print(f"The dog's age in dog’s years is {int(dog_age)} years.")
else:
    print('Thats not years')