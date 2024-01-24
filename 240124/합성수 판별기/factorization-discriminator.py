n = int(input())

satisfied = False

if n>=1:
    if n%1==0 and n%n==0:
        satisfied = True

if satisfied == True:
    print('C')
else:
    print('N')