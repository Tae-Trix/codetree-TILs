sum_val = 0
len_val = 0

while True:
    age = int(input())
    if age//10 != 2:
        break
    sum_val = sum_val + age
    len_val = len_val + 1

mean_val = sum_val/len_val
print("%.2f"%mean_val)