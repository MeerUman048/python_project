#write a python program to input all the sides of triangle and check whether the triangle is valid or not?
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and c + a > b:
    print("Valid triangle")
else:
    print("Invalid triangle")


