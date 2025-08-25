#8. Write a program to swap two numbers using third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping: a =", a, " b =", b)

# Swapping using third variable
temp = a
a = b
b = temp

print("After Swapping: a =", a, " b =", b)