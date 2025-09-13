#4. WAP to print factorial of a number.

n =int(input("Enter the number to find factorial of a number - "))
fact = 1
for i in range(1, n+1):   # goes from 1 to n
    fact *= i
print("Factorial of", n, "is:", fact)
