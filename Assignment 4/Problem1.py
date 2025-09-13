# 1. WAP to print all even numbers until n.

#using while loop
n =int(input("Enter the number to print even numbers. n = "))
i = 2
while(i<=n):
    if(i%2==0):
        print(i)
    i+=1


#using for loop
n =int(input("Enter the number to print even numbers. n = "))
for i in range (2,n+1,2):
     print(i)