i = 0
j = 0
for _ in range(10):
    a = int(input())
    if (a%3==0) and (a%5==0):
        i = i + 1
        j = j + 1
    elif(a%5==0):
        j = j + 1
    elif (a%3==0):
        i = i + 1

print(i, end = ' ')
print(j)