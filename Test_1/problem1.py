#1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:

import math
l=  float(input("Enter the length "))
b = float(input("Enter the breadth "))
#r = float(input("Enter the radius "))
r = b/2
area_rect = l*b
areaofsemi = 0.5 * math.pi *r * r
total_area = area_rect + areaofsemi
print ('area of fig is ',total_area)
perimeter =  (2 * l) + b + (math.pi * r)
print ('perimeter of fig is ',perimeter)
