#Write a Python program to input any character and check whether it is alphabet, digit or special character.
ch=input("enter any character:")
if ch.isalpha():
    print(ch,"is alphabet")
elif ch.isdigit():
    print(ch,"is digit")
else:
    print(ch,"is special character")
