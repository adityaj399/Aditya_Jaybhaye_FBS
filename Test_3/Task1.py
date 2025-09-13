#1. write a program to find first n prime numbers

n = int(input("Enter how many prime numbers you want: "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primes = []
num = 2   # start checking from 2

while len(primes) < n:   # keep finding until we get n primes
    if is_prime(num):
        primes.append(num)
    num += 1

print(f"First {n} prime numbers are: {primes}")