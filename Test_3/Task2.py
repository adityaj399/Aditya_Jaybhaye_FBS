#2. write a program to print this series where accept value of N from the user1/1! + 2/2! + 3/3! + 4/4! + …..N/N!

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def series_sum(N):
    total = 0
    for i in range(1, N+1):
        total += i / factorial(i)
    return total

N = int(input("Enter the value of N: "))
print("Sum of the series =", series_sum(N))