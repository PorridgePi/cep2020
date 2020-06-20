def egged(year, span):
    if year <= 0:
        return "No chickens yet!"

    chickens = {1: 300, 2: 300, 3: 300}

    for currentYear in range(1, year):
        if currentYear >= span:
            break

        print(chickens)

        for i in range(3*currentYear):
            i += 1
            chickens[i] = int(chickens[i]*0.8)

        nextYear = currentYear + 1
        newChicken = nextYear * 3

        for n in range(newChicken - 2, newChicken+1):
            chickens[n] = 300

    sum = 0
    for i in chickens:
        sum += chickens[i]

    return(sum)


print(egged(2,1))
print(egged(4,8))