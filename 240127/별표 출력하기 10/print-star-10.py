n = int(input())

for i in range(1,n+1):
    if i%2==0:
        for j in range(1,(n-(i-1)//2)+1):
            print('*', end = ' ')
    if i%2==1:
        for j in range(1, (i//2)+1+1):
            print('*', end = ' ')
    print()

for i in range(n,1-1, -1):
    if i%2==0:
        for j in range(1,(n-(i-1)//2)+1):
            print('*', end = ' ')
    if i%2==1:
        for j in range(1, (i//2)+1+1):
            print('*', end = ' ')
    print()