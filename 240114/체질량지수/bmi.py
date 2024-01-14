arr = input().split()
height = int(arr[0])
weight = int(arr[1])
BMI = (weight*100*100)/(height*height)
print(int(BMI))
if BMI >= 25:
    print("Obesity")