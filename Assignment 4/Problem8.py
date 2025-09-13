# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

first =int(input("Enter the range from "))
last =int(input("Enter the range to "))
print(f'numbers are divisible by 7 and multiple of 5 from {first} and {last}')

for i in range(first, last):
    if(i%7==0 and i%5==0):
        print(i)
