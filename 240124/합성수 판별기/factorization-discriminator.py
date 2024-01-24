n = int(input())

for i in range(2,n):
    if n%i==0:
        sum_num = True

if sum_num == True:
    print('C')
else:
    print('N')