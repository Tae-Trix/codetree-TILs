n = int(input())

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0

for i in range(1,n+1):
    if i%2==0:
        cnt_1 = cnt_1 + 1
        if (i%6==0) or (i%12==0):
            cnt_1 = cnt_1 - 1
        
    if i%3==0:
        cnt_2 = cnt_2 + 1
        if i%12==0:
            cnt_2 = cnt_2 - 1
    
    if i%12==0:
        cnt_3 = cnt_3 + 1


print(cnt_1, end = ' ')
print(cnt_2, end = ' ')
print(cnt_3)