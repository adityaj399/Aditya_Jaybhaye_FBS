#write a program to find print the following fibonacci series using functions:

def fibonacci(num):
    a,b = 1,1
    for i in range(num):
        print(a, end=' ')
        a,b = b,a+b
num = int(input("Enter no of terms  "))
fibonacci(num)



    