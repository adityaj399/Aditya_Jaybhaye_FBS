# 5. Write a program to find factorial using recursion.

def fact(n, i=1):
    if i == n:
        return n
    return i * fact(n, i + 1)

n = int(input("Enter n: "))
print("Factorial =", fact(n))