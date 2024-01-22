n = int(input())
val = 0
num = 0
for i in range(1,100):
    val = n//i
    n = n//i
    num = num + 1
    if val <= 1:
        break

print(num)