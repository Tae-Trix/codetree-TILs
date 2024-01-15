y = int(input())

answer = "true"

if y%4==0:
    answer = 'true'
    if y%100==0:
        answer = 'false'
        if y%400==0:
            answer = 'true'
        else:
            answer = 'false'
else:
    answer = 'false'

print(answer)