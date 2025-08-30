#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

S1 = float(input("enter the side1 of triangle "))
S2 = float(input("enter the side2 of triangle "))
S3 = float(input("enter the side3 of triangle "))


if(S1+S2>S3 and S2+S3>S1 and S1+S3>S2):
    print("it is valid triangle")
    if(S1==S2==S3):
        print("It is an equilateral triangle: ")
    elif(S1==S2 or S2==S3 or S1==S3):
        print("It is an isosceles triangle")
    else:
        print("It is Scalene triangle")
else:
    print("It is not valid triangle")        