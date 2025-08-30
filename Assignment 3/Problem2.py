#2.Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input("Enter any Alphabet : ")
if(alpha in ('a', 'e', 'i', 'o', 'u')):
    print(f"{alpha} is an vowel ")
else:
    print(f"{alpha} is an consonent")