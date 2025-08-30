#7. Write a program to check if user has entered correct userid and password.

userid = input("Enter the UserID : ")
password = input("Enter the Password : ")

if(userid == 'adi123' and password == '@shra123'):
    print("Sucessfully Login")
else:
    print('Invalid username & Password')    