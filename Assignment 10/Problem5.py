# 5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

lst = [1, 2, 3, 2, 4, 2, 5]
num = int(input("Enter number to search: "))

count = 0
for i in lst:
    if i == num:
        count += 1

if count > 0:
    print(num, "is present", count, "times")
else:
    print(num, "not found")