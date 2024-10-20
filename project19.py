#write a program to check if student is either passed or failed?
math=int(input("enter the marks in math="))
science=int(input("enter the marks in science="))
english=int(input("enter the marks in english="))
urdu=int(input("enter the marks in urdu="))
computer=int(input("enter the marks in computer="))
MarksObtained=math+science+english+urdu+computer
percent=(MarksObtained/500)*100
if(percent>=75):
    grade="DISTINCTION"
elif(percent>=60):
    grade="A"
elif(percent>=50):
    grade="B"
elif(percent>=33):
    grade="C"
else:
    grade="fail"
print("grade obained by student is:",grade)
