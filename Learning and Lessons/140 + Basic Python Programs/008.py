#Write a Python program to display calendar.
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month) 
#Quais as outras propriedades de calendar?
print(cal)