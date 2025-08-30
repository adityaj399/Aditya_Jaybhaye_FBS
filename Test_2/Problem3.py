# A farmer has a field which is half in circle share and rest rectangle.He needs to do fencing for entire field using barbed wire 5 times.
# Circular section has radius 20m and rectangle length is 50m & breadth is 40m. if cost of barbed wire is 35rs/m then calculate
# the total cost of fencing the fielding.

length = 15
breadth = 10

radius = 20

perimeter_circle = 2 * 3.14 * radius

perimeter_rect = 2 * (length*breadth)

total_fencing = (perimeter_circle * perimeter_rect) * 5

total_cost = total_fencing * 35

print("Total cost of fencing = Rs. ",total_cost)