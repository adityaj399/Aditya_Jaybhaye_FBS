# 2. WAP to print all odd numbers until n.

#Using While Loop
n =int(input("Enter the number to print odd numbers. n = "))
i = 1
while(i<=n):
    if(i%2 != 0):
        print(i)
    i+=1   

#Using For loop
n =int(input("Enter the number to print odd numbers. n = "))
for i in range(1,n+1,2):
        print(i)
