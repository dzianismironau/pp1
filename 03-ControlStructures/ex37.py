pattern = str()

for i in range(1,6):
    pattern += ' *'
    print(pattern)
    i += 1

for n in range(1,5):
        pattern = pattern[:-2]
        print(pattern)
        i += 1
