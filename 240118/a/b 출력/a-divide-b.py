arr = input().split()

a = int(arr[0])
b = int(arr[1])

i = 1
if a//b == 0:
    print(0,end ='')
    print(".", end = '')
    while i <= 20:
        c = (a*10)//b
        a = (a*10)%b
        print(int(c), end = '')
        i = i + 1
elif a//b == 1:
    print(1, end = '')
    print(".", end = '')
    while i <= 20:
        c = (a*10)//b
        a = (a*10)%b
        print(int(c), end = '')
        i = i + 1