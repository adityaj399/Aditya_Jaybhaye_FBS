# 11. Write a program to print all numbers which are divisible by m and n in the list.
lst = [10,72,46,20,32,40,50,40]
m = 5
n = 10

for i in lst:
    if i % m == 0 and i % n == 0:
        print(i)