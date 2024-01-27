n = int(input())

for i in range(0, n):
    for j in range(0,-1*i + 2):
        print(' ', end = '')
    for j in range(0, i+1):
        print('*', end = ' ')
    print()

for i in range(n-2,-1,-1):
    for j in range(0,-1*i + 2):
        print(' ', end = '')
    for j in range(0, i+1):
        print('*', end = ' ')
    print()