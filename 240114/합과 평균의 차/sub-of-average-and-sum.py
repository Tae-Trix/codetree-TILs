arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
num = a,b,c
print(sum(num))
print(int(sum(num)/len(num)))
print(sum(num) - int(sum(num)/len(num)))