#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = float(input("Enter the marks scored in M1 - "))
m2 = float(input("Enter the marks scored in M2 - "))
m3 = float(input("Enter the marks scored in M3 - "))
m4 = float(input("Enter the marks scored in M4 - "))
m5 = float(input("Enter the marks scored in M5 - "))

total = m1+m2+m3+m4+m5
percentage = (total/500)*100

print("Total Marks is ",total)
print("percentage obtained is ",percentage)

if(percentage > 80):
    print("Passed with First class ")
elif(percentage >60):
    print("Passed with Second class ")
elif(percentage > 35):
    print("Passed  ")
else:
    print("Failed")