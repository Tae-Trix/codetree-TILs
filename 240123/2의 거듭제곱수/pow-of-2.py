n = int(input())
m = 0

while True:
    if n//2==1:
        m = m + 1
        break
    n = n//2
    m = m + 1
print(m)