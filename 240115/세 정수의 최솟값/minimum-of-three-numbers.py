arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
value = int(a)

if a<=b and b<=c:
    value = a
elif b<=c and b<=a:
    value = b
elif c<=a and c<=b:
    value = c
print(value)