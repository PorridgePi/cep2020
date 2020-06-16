def num2date(day):
    month=''
    months = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
        }
    for i in months:
        if day-months[i] > 0:
            day-=months[i]
        else:
            month=i
            break
    return month+' '+str(day)

print(num2date(365))