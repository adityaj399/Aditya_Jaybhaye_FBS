"""#8. Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)"""

import random

userid = input("Enter the UserID : ")
password = input("Enter the Password : ")
if(userid == 'adi123' and password == '@shra123'):

    captcha = random.randint(1111,9999)
    print(f"Captcha: {captcha}")

    user_cap = int(input("Enter the caotcha shown above : "))
    
    if(captcha == user_cap):
        print("Sucessfully login")
    else:
        print("wrong captcha")  

else:
    print("Invalid UserID & Password")
        