arr = input().split()
a = int(arr[0])
b = int(arr[1])

if a>0:
    while b!=0:
        print(a, end = '')
        b = b-1
elif a<=0:
    print(0)