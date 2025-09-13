#3. program to accept n number of employees from user and accept basic salary of employee . if the salary is less than 20000 
# then da: 10% , ta: 12% and hra: 15% otherwise da:15%, ta:18% and hra: 20% 
# and find total salary of employees and find the total salary of all employees

n = int(input("Enter number of employees: "))

grand_total = 0

for i in range(1, n+1):
    print(f"\nEmployee {i}:")
    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.15
    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20

    total = basic + da + ta + hra
    print(f"Total salary of Employee {i} = {total:.2f}")

    grand_total += total

print("\n------------")
print("Total salary of all employees =", grand_total)



