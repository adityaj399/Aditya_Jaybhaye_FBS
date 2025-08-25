#5. Write a program to enter P, T, R and calculate Compound Interest.

P = float(input("Enter the Principal amt "))
T = float(input("Enter the Time "))
R = float(input("Enter the Rate of int. "))

CI = P*((1+R/100)**T)- P
print ('Compound Interest is ', CI)