n = int(input())
sum_val = 0
len_va = 0
for _ in range(n):
    a = int(input())
    sum_val = sum_val + a
    len_va = len_va + 1

mean_val = sum_val / len_va

print(sum_val, end = ' ')
print("%.1f"%mean_val)