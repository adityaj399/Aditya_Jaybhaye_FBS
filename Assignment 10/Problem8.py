# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

list = [32,45,36,43,12,54]
list2 = []

for i in list:
    #list == list2
    list2.append(i)

print(list2)    