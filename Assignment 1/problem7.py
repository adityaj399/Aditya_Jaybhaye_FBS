#7. Program to Find the Roots of a Quadratic Equation

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

root1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)

print("Root 1 =", root1)
print("Root 2 =", root2)