#5. Sum of all prime numbers between 1 to n

n = int(input("Enter a number: "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
    total = 0
    for i in range(1, n+1):
        if is_prime(i):
            total += i
    return total

print(f"Sum of all prime numbers between 1 and {n} is {sum_primes(n)}")