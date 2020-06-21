# def printCalendar(year,month,day):

from math import floor

year = 2020
month = 6
day = 21

if (year % 4 == 0) and (not (year % 100 == 0) or year % 400):
    leapYear = True
else:
    leapYear = False

centuryDigits = int(str(year)[:2])
yearDigits = int(str(year)[2:4])

value = yearDigits + floor(yearDigits / 4)

if centuryDigits == 18: value += 2
elif centuryDigits == 20: value += 6

if month == 10 or (month == 1 and not leapYear):
    value += 1
elif month == 8 or (month == 2 and leapYear):
    value += 3
elif month == 3 or month == 11 or (month == 2 and not leapYear):
    value += 4
elif month == 4 or month == 7:
    pass
elif month == 5:
    value += 2
elif month == 9 or month == 12:
    value += 6
elif month == 6:
    value += 5

weekDay = (value + day + 6) % 7





pass
