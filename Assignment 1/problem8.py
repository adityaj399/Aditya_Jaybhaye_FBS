#8. Write a program to convert days into years, weeks and days.
d = int(input("No. Of Days are  "))
y = d//365
d = d%365
w = d//7







print('No. Of years are - ', y)
print('No. Of days are - ', d)
print('No. Of Weeks are - ', w)