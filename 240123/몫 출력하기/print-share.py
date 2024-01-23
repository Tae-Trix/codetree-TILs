i = 0
while True:
    n = int(input())
    if n%2==0:
        print(n//2)
        i = i + 1
        if i == 3:
            break
    elif n%2==1:
        continue