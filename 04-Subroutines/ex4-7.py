def computegrade(score):
    grade = ''
    try:
        score = float(enter_score)
    except:
        grade = 'Bad score'

    if float(score) > 1:
        grade = 'Bad score'
    elif float(score) >= 0.9:
        grade = 'A'
    elif float(score) >= 0.8:
        grade = 'B'
    elif float(score) >= 0.7:
        grade = 'C'
    elif float(score) >= 0.6:
        grade = 'D'
    elif float(score) < 0.6:
        grade = 'F'

    return grade

enter_score = input('Enter score: ')

print(f'{computegrade(enter_score)}')