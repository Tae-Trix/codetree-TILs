sum_val = 0
len_val = 0

for _ in range(10):
    a = int(input())
    if (a>=0) and (a<=200):
        sum_val = sum_val + a
        len_val = len_val + 1

mean_val = sum_val/len_val

print(sum_val, end = ' ')
print("%.1f"%mean_val)