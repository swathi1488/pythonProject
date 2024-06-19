side1 = float(input("enter length of a triangle is:\n"))
side2 = float(input("enter lenth of a triangle is:\n"))
side3 = float(input("enter length of a triangle is:\n"))

if side1 == side2 == side3:
    print("eq")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("isosceles")
else:
    print("scales")
    print("scales")
