
#Write a Python program to print the calendar of a given month and year.

import calendar
year = int(input("enter a year : "))
month = int(input("enter a month : "))

calendar = calendar.month(year,month)
print(calendar)

