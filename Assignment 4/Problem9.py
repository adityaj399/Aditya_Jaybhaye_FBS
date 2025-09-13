# 9. WAP to print all numbers in a range divisible by a given number.

n =int(input("Enter the number "))

first =int(input("Enter the range from "))
last =int(input("Enter the range to "))
print(f'numbers are divisible by {n}')

for i in range(first, last):
    if(i%n==0):
        print(i)
