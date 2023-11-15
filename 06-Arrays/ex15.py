arr = [[1,3,5],[8,7,2]]

#a
sum = arr[0][0] + arr[-1][-1]
print(sum)

#b
sum1 = arr[0][1] + arr[1][1]
print(sum1)

#c
sum2 = 0
for i in arr[-1]:
    sum2+=i
print(sum2)