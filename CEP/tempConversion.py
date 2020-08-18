
#temperature conversion program
#Celsius - Fahrenheit / Fahrenheit - Celsius

def displayWelcome():
    print("""This program will convert a range of temperatures
Enter (F) to convert Fahrenheit to Celsius
Enter (C) to convert Celsius to Fahrenheit\n """)

def getConvertTo():
    to=input("Enter selection: ")
    fromTemp=input("Enter starting temperature to convert: ")
    toTemp=input("Enter ending temperature to convert: ")
    return to, fromTemp, toTemp
    #your code here

def displayFahrenToCelsius(start,end):
    for i in range(start,end+1):
        t=(i-32)*5/9
        if i>=100:
            print("   "+format(i,'.1f')+"   "+format(t,'.1f'))
        else:
            print("   "+format(i,'.1f')+"    "+format(t,'.1f'))

def displayCelsiusToFahren(start,end):
    for i in range(start,end+1):
        t=i/5*9+32
        if t>100:
            print("   "+format(t,'.1f')+"   "+format(i,'.1f'))
        else:
            print("   "+format(t,'.1f')+"    "+format(i,'.1f'))


def main():
    displayWelcome()
    choice=getConvertTo()
    print("\n  Degrees  Degrees\nFahrenheit Celsius")
    if choice[0]=="F":
        displayFahrenToCelsius(int(choice[1]),int(choice[2]))
    elif choice[0]=="C":
        displayCelsiusToFahren(int(choice[1]),int(choice[2]))

main()   #calling main function
