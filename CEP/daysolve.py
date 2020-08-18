date = input("Enter date in YYYYMMDD format: ")
while len(date)!=8:
    date = input("Enter date in YYYYMMDD format: ")

value = 0

yr = int(date[0:4])
c = int(date[0:2])
y = int(date[2:4])
m = int(date[4:6])
d = int(date[6:8])
leap = y%4==0 and yr%100 != 0 or yr%400 == 0

val = y+y//4 

if c == 18: val+=2
elif c == 20: val+=6

if m == 1 and not leap: val+= 1
elif m == 2 and leap: val += 3
elif m == 2 and not leap: val += 4  
elif m == 3 or m == 11: val += 4
elif m == 5: val += 2
elif m == 6: val += 5 
elif m == 8: val += 3 
elif m == 10: val += 1
elif m == 9 or m == 12: val += 6

val = (val+d)%7

weekDay = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
day = weekDay[val]

print(day)