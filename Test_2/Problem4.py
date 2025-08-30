# Write a program to calculate the total cost of painting. the interior of building with four equal sized walls.

l = float(input("Enter the length of a wall :"))
h = float(input("Enter the hieght of a wall :"))

cost_per_sqm = float(input("enter the cost of painting per square meter :"))

area_onewall = l* h

total_area = 4 * area_onewall
total_cost = total_area * cost_per_sqm

print("Total cost of painting the interior is Rs. ",total_cost)