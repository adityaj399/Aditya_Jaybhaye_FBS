"""4. Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
exterior wall."""

wall_area = float(input("Enter the area of one wall "))
interior_cost = float(input("cost of interior wall "))
exterior_cost = float (input("Cost of Exterior wall "))

total_walls = 8
common_walls = 2
exterior_walls = total_walls - common_walls 
interior_walls = total_walls

total_interior_cost = interior_walls * wall_area * interior_cost 
total_exterior_cost = exterior_walls * wall_area * exterior_cost 

print("Total Interior Painting Cost = ",total_interior_cost)
print("Total Exterior Painting Cost = ",total_exterior_cost)