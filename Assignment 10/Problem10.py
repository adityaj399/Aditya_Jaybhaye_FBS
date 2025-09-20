# 10. Write a program to remove all occurrences of a given element in the list.

lst = [1, 2, 3, 2, 4, 2, 5]
num = int(input("Enter element to remove: "))

new_list = []
for i in lst:
    if i != num:
        new_list.append(i)

print("List after removing", num, "=", new_list)