n = int(input())

satisfied = True

if n>1:
    if n%1==0 and n%n==0:
        satisfied = False

if satisfied == False:
    print('C')
else:
    print('N')