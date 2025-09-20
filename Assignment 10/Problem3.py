# 3. Write a program to find the second largest element in the list.

list = [34,56,23,77,57,89]

max = 0
sec_max = 0

for i in list:
    if i > max:
        sec_max = max
        max = i
    elif i > sec_max and i != max:
        sec_max = i

print(sec_max, 'is the second largest element')        

