height = input('Enter your height: ')
inFeet = int(height)/30.48
inInches = (inFeet - int(inFeet))*12

print(f'I am {height} cm tall, i.e. {int(inFeet)} feet and {int(inInches)} inches')
