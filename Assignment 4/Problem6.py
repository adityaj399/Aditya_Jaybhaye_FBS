# 6. WAP to check if a given number is prime number or not.

n =int(input("Enter the number "))
for i in range(2,n):
    if(n%i==0):
        print("It is not a Prime number")
        break
else:
    print("It is a Prime number")        