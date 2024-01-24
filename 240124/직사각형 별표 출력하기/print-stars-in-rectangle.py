arr = input().split()
a = int(arr[0])
b = int(arr[1])

for _ in range(a):
    for _ in range(b):
        print("*", end = ' ')
    print()