'''8. Write a program to solve the following series :
a. 1! + 2! + 3! + 4! + .....n!
b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
e. x - x2/3 + x3/5 - x4/7 + .... to n terms'''


def factorial_series(n):
    def fact(num):
        f = 1
        for i in range(1, num+1):
            f *= i
        return f
    total = 0
    for i in range(1, n+1):
        total += fact(i)
    return total

def power_series(N):
    total = 0
    for i in range(1, N+1):
        total += N**i
    return total

def geometric_series(n):
    total = 0
    term = 1
    for i in range(n):
        total += term
        term *= 2
    return total

def custom_series_d(a):
    total = 0
    for i in range(1, 11):
        total += (a**i) / i
    return total

def alternating_series(x, n):
    total = 0
    sign = 1
    denominator = 1
    for i in range(1, n+1):
        total += sign * (x**i) / denominator
        sign *= -1
        denominator += 2
    return total

n = int(input("Enter value of n: "))
print("a. Sum of factorial series =", factorial_series(n))
print("b. Power series sum =", power_series(n))
print("c. Geometric series sum =", geometric_series(n))

a = int(input("\nEnter value of a for series (d): "))
print("d. Custom series sum =", custom_series_d(a))

x = int(input("\nEnter value of x for series (e): "))
print("e. Alternating series sum =", alternating_series(x, n))
