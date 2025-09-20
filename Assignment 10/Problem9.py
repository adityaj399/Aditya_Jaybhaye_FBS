'''# 9. Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements.'''

list = [32,22,9,21,45]
even =[]
odd =[]

for i in list:
    if  i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("original list",list)
print('even :',even)
print('odd :',odd)