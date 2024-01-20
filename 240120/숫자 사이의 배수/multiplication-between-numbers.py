arr = input().split()
a = int(arr[0])
b = int(arr[1])

sum_val = 0
len_val = 0

for i in range(a,b+1):
    if (i%5==0) or (i%7==0):
        sum_val = sum_val + i
        len_val = len_val + 1

mean_val = sum_val/len_val
print(sum_val, end = ' ')
print('%.1f'%mean_val)