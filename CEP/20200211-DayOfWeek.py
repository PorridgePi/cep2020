def day_of_week(month,day,year):
    value = 0

    c = int(str(year)[0:2])
    y = int(str(year)[2:4])

    leap = y%4==0 and year%100 != 0 or year%400 == 0

    val = y+y//4 

    if c == 18: val+=2
    elif c == 20: val+=6

    if month == 1 and not leap: val+= 1
    elif month == 2 and leap: val += 3
    elif month == 2 and not leap: val += 4  
    elif month == 3 or month == 11: val += 4
    elif month == 5: val += 2
    elif month == 6: val += 5 
    elif month == 8: val += 3 
    elif month == 10: val += 1
    elif month == 9 or month == 12: val += 6

    val = (val+day)%7

    weekDay = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    return weekDay[val]

