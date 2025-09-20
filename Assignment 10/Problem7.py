# 7. Write a program to create a new list from existing list which contains cube of each number of list.

lst = [1, 2, 3, 4, 5]
cube_list = []

for i in lst:
    cube_list.append(i**3)

print("Cube List =", cube_list)