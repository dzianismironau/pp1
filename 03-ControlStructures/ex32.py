science = input('Are you interested in computer science? (Y/N): ')
games = input('Do you like playing computer games? (Y/N): ')
inst = input('Do you have an Instagram account? (Y/N): ')

if science == 'Y':
    science = 'Yes'
else:
    science = 'No'

if games == 'Y':
    games = 'Yes'
else:
    games = 'No'

if inst == 'Y':
    inst = 'Yes'
else:
    inst = 'No'

print(f'Inerested in computer science: {science}\nPlaying computer games: {games}\nHas an Instagram account: {inst}')