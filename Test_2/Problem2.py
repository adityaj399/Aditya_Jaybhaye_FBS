#WAP to accept three digit number. if first digit is doubled of second digit and half of third digit 
# then display"Yes, u have done it", otherwis print "Please try later"

num = int(input("Enter Three digit Number : "))

hundreds = num // 100
tens =( num % 100) //10
units = num % 10

if ((hundreds == tens+tens) and (hundreds == units - hundreds)):
    print("Yes, you have done it ")

else:
    print("Please try later ")