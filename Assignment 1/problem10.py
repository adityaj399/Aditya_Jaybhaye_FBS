#10. Write a program to calculate area of an equilateral triangle.

import math

a = float(input("Enter the side of the equilateral triangle: "))

area = (math.sqrt(3) / 4) * (a ** 2)

print("Area of the equilateral triangle is:", area)