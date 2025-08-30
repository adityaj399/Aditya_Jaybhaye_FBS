# WAP to accept year from user and check if it is leap year or not

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")
