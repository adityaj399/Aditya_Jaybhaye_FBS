#6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

bs = int(input("Enter the Basic Salary - "))
da = (10/100)*bs
print("da of basic salary is -",da)
ta = (12/100)*bs
print("da of basic salary is -",ta)
hra = (15/100)*bs
print("da of basic salary is -",hra)

total_salary = bs + da + ta + hra
print("Total Salary of Employee is -", total_salary)

