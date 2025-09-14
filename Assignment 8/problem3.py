'''3. Write a program to find sum of following series using functions :
a. 1+ 2 + 3 + 4+..... + n
b. 1!+ 2! + 3! + 4!+..... + n!
c. 1^1 + 2^2 + 3^3+ ...... n^n'''

n = int(input("Enter the digit to count the numbers: "))

def digitcount():
    sum= 0
    for i in range(1,n+1):
        sum += i
    print(f'sum of {n} digits is',sum)
       

digitcount()   


def sum_factorials(n):
    total = 0
    for i in range(1, n+1):
        fact = 1
        for j in range(1, i+1):   # calculate i!
            fact *= j
        total += fact
    return total

