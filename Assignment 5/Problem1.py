#1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_userid = "admin"
correct_password = "1234"

for attempt in range(3):
    userid = input("Enter userid: ")
    password = input("Enter password: ")

    if userid == correct_userid and password == correct_password:
        print("✅ Login Successful!")
        break
    else:
        print("❌ Wrong credentials, try again.")

else:
    print("⚠️ Program terminated! Too many failed attempts.")
