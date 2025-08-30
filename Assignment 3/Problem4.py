#4. 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = float(input("Enter 1st Side of trainlge  "))
b = float(input("Enter 2nd Side of trainlge  "))
c = float(input("Enter 3rd Side of trainlge  "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is valid")

else:
    print("Trianlge is not valid")    
