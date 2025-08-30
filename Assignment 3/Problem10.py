#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter Male Or Female ")
age = int(input("Enter the age "))

if(gender == 'M'):
    if(age >=21):
        print("Eligible to marraige")
    else:
        print("Not Eligible to marraige")
else:
    if(age > 17):
        print('Eligible to marraige')
    else:
        print('Not Eligible to marraige')
