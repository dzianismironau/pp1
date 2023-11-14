import mykeyboard 
import mymath

user_guess = mykeyboard.read_number()
computer_guess = mymath.generate_number()
if user_guess == computer_guess:
    print(f'Computer number: {computer_guess}\nYou won the game!!')
else:
    print(f'Computer number: {computer_guess}\nTry one more time!')
