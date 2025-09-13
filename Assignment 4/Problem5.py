#5. WAP to print Fibonacci series upto n.

n =int(input("Enter the number "))
a,b = 0,1 
for i in range(1,n):
    print(a,end=" ")
    a,b=b,a+b
    