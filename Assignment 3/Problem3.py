#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

A1 = float(input("Enter 1st Angle of trainlge  "))
A2 = float(input("Enter 2nd Angle of trainlge  "))
A3 = float(input("Enter 3rd Angle of trainlge  "))

if( A1 + A2+ A3 == 180):
    print("Given angles are valid and it is a Triangle")

else:
    print("Given angles are not valid and it is not a Triangle")    

