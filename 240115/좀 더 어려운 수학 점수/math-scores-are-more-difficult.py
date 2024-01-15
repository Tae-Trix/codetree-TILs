A = input().split()
A_math = int(A[0])
A_eng = int(A[1])

B = input().split()
B_math = int(B[0])
B_eng = int(B[1])

name = "A"

if A_math > B_math:
    name = "A"
elif A_math < B_math:
    name = "B"
elif A_math == B_math:
    if A_eng > B_eng:
        name = "A"
    elif A_eng < B_eng:
        name = "B"

print(name)