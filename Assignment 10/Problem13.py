# 13 . Write a program to print list after removing even numbers.
lst = [1, 2, 3, 4, 5, 6, 7]
new_list = []

for i in lst:
    if i % 2 != 0:
        new_list.append(i)

print("List after removing even numbers =", new_list)