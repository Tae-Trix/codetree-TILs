arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

mid = 0

if (b<a and a<c) or (c<a and a<b):
    mid = a
if (a<b and b<c) or (c<b and b<a):
    mid = b
if (a<c and c<b) or (b<c and c<a):
    mid = c
    
print(mid)