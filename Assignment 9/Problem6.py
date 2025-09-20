# 6. Write a program to print Fibonacci series using recursion.

def print_fib(a, b, n):
    if n == 0:
        return
    print(a, end=" ")
    print_fib(b, a + b, n - 1)

n = int(input("Enter number of terms: "))
print("Fibonacci Series:")
print_fib(0, 1, n)

