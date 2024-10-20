#Write a python program to calculate profit or loss ?
from tkinter.ttk import Label

CP=int(input("enter cost price"))
SP=int(input("enter selling price"))
profit=SP-CP
if(profit>0):
    print("profit of",profit)
elif (profit<0):
    print("loss of",profit)
else:
    print("no loss or profit")



