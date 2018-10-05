#3. Write a Python program to display the current date and time.


import datetime

print(datetime.datetime.now())

#Write a Python program to calculate number of days between two dates
date1 = datetime.date(1999,10,1)
date2 = datetime.date(1999,10,10)
days = date2 - date1
print(days.days)





