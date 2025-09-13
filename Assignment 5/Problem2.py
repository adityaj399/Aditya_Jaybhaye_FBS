#2. Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

Students = int(input("Enter number of students : "))

for Students in range(Students):
  print('Enter marks of 5 subjects ')
  M1= int(input('M1 = '))
  M2= int(input('M2 = '))
  M3= int(input('M3 = '))
  M4= int(input('M4 = '))
  M5= int(input('M5 = '))

  percentage = (M1+M2+M3+M4+M5)/500 *100
  print(f'percentage is :',percentage)
