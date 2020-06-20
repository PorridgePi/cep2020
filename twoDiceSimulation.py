from random import randint


def roll():
    return randint(1, 6)+randint(1, 6)


def main():
    combinations = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    rolls = {}
    for i in range(2, 13):
        rolls[i] = 0

    i = 2
    n = roll()
    rolls[n] = 1

    for i in range(1000):
        n = roll()

        if n in rolls:
            rolls[n] += 1

    print("Total:   Simulated(Percent)  Expected(Percent)")

    for i in rolls:
        simulated = str(format(rolls[i]/1000*100, '.2f'))
        expected = str(format(combinations[i]/36*100, '.2f'))
        print(str(i)+'\t\t'+simulated+'\t\t'+expected)


main()
