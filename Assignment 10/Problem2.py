# 2. Write a program to find maximum and minimum element in a list

list = [22,9,45,18,24,65]

maximum = list[0]
minimum = list[0]

for i in list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)
   
    