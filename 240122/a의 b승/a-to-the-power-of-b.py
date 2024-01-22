arr = input().split()
a = int(arr[0])
b = int(arr[1])
prod = 1

while b>=1:
    prod = prod * a
    b = b - 1

print(prod)