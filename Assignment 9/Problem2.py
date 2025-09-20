#2. Write a program to check if given number is Armstrong or not using recursive

def armstrong(num,digits):
    if num == 0:
        return 0
    return (num%10) ** digits + armstrong(num//10,digits)

n = int(input("Enter number "))
digits = len(str(n))

if armstrong(n,digits) == n:
    print("Armstrong number ")
else:
    print("Not Armstrong")    