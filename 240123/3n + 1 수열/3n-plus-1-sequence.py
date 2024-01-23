n = int(input())
num = 0
while True:
    if n==1:
        break
    elif n%2==0:
        n = n/2
        num = num + 1
        if n==1:
            break
    elif n%2==1:
        n = 3*n + 1
        num = num + 1
        if n==1:
            break
print(num)