arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

max_val = 0

if a>=b and a>=c:
    max_val = a
elif b>=c and b>=a:
    max_val = b
elif c>=a and c>=b:
    max_val = c
print(max_val)