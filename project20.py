#Write a Python program to input basic salary of an employee and calculate its Gross salary according to following:
#Basic Salary <= 10000 : HRA = 20%, DA = 80%
#Basic Salary <= 20000 : HRA = 25%, DA = 90%
#Basic Salary > 20000 : HRA = 30%, DA = 95%
basic_salary=float(input("enter basic salary"))
if basic_salary<=10000:
    hra=0.20*basic_salary
    da=0.80*basic_salary
elif basic_salary<=20000:
    hra=0.25*basic_salary
    da=0.90*basic_salary
else:
    hra=0.30*basic_salary
    da=0.95*basic_salary
Gross_Salary=basic_salary+hra+da
print("The gross salary of he employee is",Gross_Salary)

