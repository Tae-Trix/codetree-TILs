A = input().split()
A_math = int(A[0])
A_eng = int(A[1])

B = input().split()
B_math = int(B[0])
B_eng = int(B[1])

if A_math > B_math and A_eng > B_eng:
    print(1)
else:
    print(0)