# 6. Write a program to remove duplicates from the list.

list = [23,45,67,23,85,67]
unique = []

for i in list:
    if i not in unique:
      unique.append(i)

print (unique)