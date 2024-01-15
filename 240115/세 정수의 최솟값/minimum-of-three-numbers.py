arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a<b and a<c and b!=c:
    print(a)
if b<c and b<a and c!=a:
    print(b)
if c<a and c<b and a!=b:
    print(c)

if a==b and a!=c and b!=c:
    print(a)
if b==c and b!=a and c!=a:
    print(b)
if c==a and c!=b and a!=b:
    print(c)

if a==b and b==c and c==a:
    print(a)