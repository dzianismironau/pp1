fb = input('Do you use facebook? (Yes/No): ')
tw = input('Do you use twitter? (Yes/No): ')
inst = input('Do you use twitter? (Yes/No): ')

fb_ans = bool
tw_ans = bool
inst_ans = bool

if fb == 'Yes' or fb == 'yes':
    fb_ans = True
else:
    fb_ans = False

if tw == 'Yes' or tw == 'yes':
    tw_ans = True
else:
    tw_ans = False

if inst == 'Yes' or inst == 'yes':
    inst_ans = True
else:
    inst_ans = False

if fb_ans and inst_ans or fb_ans and tw_ans or tw_ans and inst_ans:
    print('A person can be a good influenser!')
else:
    print("I'm so sorry")