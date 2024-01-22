n = int(input())
val = 0

for i in range(1, n+1):
    if (i%2==0) or (i%3==0) or (i%5==0):
        val = val + 0
        continue
    val = val + 1

print(val)