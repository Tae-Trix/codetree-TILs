a = int(input())
if a%2!=0:
    a = (a+1)/2
    print(int(a))
if a%2==0:
    a=a/2
    if a%2!=0:
        a=(a+1)/2
        print(int(a))