def printCalendar(year,month):

    from math import floor

    day = 1

    if (year % 4 == 0) and (not (year % 100 == 0) or year % 400):
        leapYear = True
    else:
        leapYear = False

    if month in (1, 3, 5, 7, 8, 10, 12):
        numDaysInMonth = 31
    elif month in (4, 6, 11):
        numDaysInMonth = 30
    elif leapYear:
        numDaysInMonth = 29
    else:
        numDaysInMonth = 28

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

    weekDay = (value + day) % 7

    if weekDay == 0:
        startingCol = 7
    else:
        startingCol = weekDay

    currentCol = 1
    columnWidth = 4
    blankChar = ' '
    blankCol = format(blankChar, str(columnWidth))

    while currentCol <= startingCol:
        print(blankCol,end = '')
        currentCol += 1

    currentDay = 1

    while currentDay <= numDaysInMonth:
        if currentDay < 10:
            print(format(blankChar, '3') + str(currentDay), end = '')
        else:
            print(format(blankChar, '2') + str(currentDay), end = '')
        
        if currentCol <= 7:
            currentCol += 1
        else:
            currentCol = 1
            print()
        
        currentDay += 1

printCalendar(2020,5)