arr_1 = input().split()
sym_1 = arr_1[0]
tem_1 = int(arr_1[1])

arr_2 = input().split()
sym_2 = arr_2[0]
tem_2 = int(arr_2[1])

arr_3 = input().split()
sym_3 = arr_3[0]
tem_3 = int(arr_3[1])

emer = 0

if sym_1 == "Y" and tem_1 >= 37:
    emer = emer + 1
if sym_2 == "Y" and tem_2 >= 37:
    emer = emer + 1
if sym_3 == "Y" and tem_3 >= 37:
    emer = emer + 1

if emer >= 2:
    print("E")
else:
    print("N")