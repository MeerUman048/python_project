#write a program to check whether a character is alphabet or not ?
letter=input("enter any alphabet:")
if(letter>="a") and (letter<="z"):
    print(letter,"is alphabet")
elif(letter>="A") and (letter<="Z"):
    print(letter,"is alphabet")
else:
    print(letter,"is not an alphabet")

