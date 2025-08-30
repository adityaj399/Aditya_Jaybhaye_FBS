#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter the three digit no. "))

hundreds = num // 100
units = num % 10

if (hundreds == units):
    print ("It is a Palindrone ")
else:
    print("It is not a palindrone ")    

