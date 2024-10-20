#write a program to input month number and number of days in that month?
month=int(input("enter month number:"))
if month==2 :
    print("28 or 29 days")
elif  month==4 or month==6 or month==9 or month==11 :
    print("30 days")
elif month>12 or month<1 :
    print("invalid month")
else:
    print("31 days")

