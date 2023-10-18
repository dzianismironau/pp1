import random
dice = random.randint(1,6)
guess = input('Guess the number: ')

print(dice == int(guess))