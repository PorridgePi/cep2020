from random import randint

done = False
coins = [1,5,10,20,50]
msg = """The purpose of this exercise is to enter a number of coin values that add up to a displayed target value. 

Enter coins values as 1 cents, 5 cents, 10 cents, 20 cents and 50 cents.
Hit return after the last entered coin value. 
----------------"""

print(msg)

while not done:
    total = randint(1,99)
    
    userInput = -1
    userTotal = 0
    
    print("Enter coins that add up to "+str(total)+" cents, one per line.\n")
    
    while True:
        if userTotal == 0:
            userInput = input("Enter first coin: ")
        else:
            userInput = input("Enter next coin: ")
            
        if userInput != "":
            try:
                userInput = int(userInput)
                if userInput not in coins:
                    print("Invalid entry")
                else:
                    userTotal+=userInput
            except ValueError:
                print("Please enter a number")
        else:
            break
    
    if userTotal>total:
        print("Sorry - total amount exceeds",userTotal-total,"cents.")
    elif userTotal<total:
        print("Sorry - you only entered",userTotal,"cents.")
    elif userTotal==total:
        print("Correct!")
        
    retry = 0 
    while retry != "y" and retry != "n":
        retry = input("\nTry again (y/n)?: ")
    if retry == "n":
        break

print("Thanks for playing ... goodbye")