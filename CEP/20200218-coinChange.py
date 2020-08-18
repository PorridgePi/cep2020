target = int(input('Enter target: '))
i = 0
while True:
    num = 3**i
    if target>num:
        print(num)
        break
    else:
        i+=1
