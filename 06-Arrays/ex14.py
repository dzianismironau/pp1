arr = [[2,5,4],[9,0,3]]

#a
print(arr)

#b
print(len(arr), len(arr[0]))

#c
print(arr[0][1])

#d
print(arr[1][2])

#e
k = ''
for row in arr[1]:
        k += str(row) + ' '
print(k)