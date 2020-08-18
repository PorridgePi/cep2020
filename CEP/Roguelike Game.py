import math
import time
import random

#Declare all global variables for ease of access
max_hp = 100
player_hp = 100
weapons = (("Wood Sword", 15),("Iron Sabre", 25),("Void Blade", 33),("Eternity", 9999))
armors = (("Rugged Clothes",5), ("Polished Armor",10), ("Shade Cloak" ,20), ("Auric Armor", 9999))
oldman_index = 0
spec_chars = ("K","O","B","G","T","C")
enemies =("B","T","G")
inventory = [["Keys > ",0 ],["Rubies > ",0 ], ["Health Pots > ", 3], ["Weapon: ","Wood Sword"],["Armour: ", "Rugged Clothes"]]
sceneChange = False
gameOver = [False, "Nil"]

#The menu screen for the shop
def shop():
    
    print_slow("\nLooking to buy some supplies?")
    print_slow("You're in the right place")
        
    while True:

        print_slow("\nType \'help\' for avaliable SHOP commands")
        cmd = str(input(">>> "))

        if cmd == "help":
            print_slow("\nAvaliable Commands:")
            print( "\nhelp > Display avaliable commands", "display > Shows the itemnumber and info of items on sale", "buy [itemnumber] > Buy an item. For Example, buy 1, buys 3 health pots", "quit > Leave the shop", sep = "\n" , end = "\n")


        elif cmd == "display":
            print_slow("\nAvaliable Items:")
            print("\n1 - 3 Health Pots [15 Rubies]", "2 - Iron Sabre (25 Attack)[30 Rubies]", "3 - Polished Armor (10 Defence)[30 Rubies]", "4 - Void Blade (33 Attack)[43 Rubies]", "5 - Shade Cloak (20 Defence)[50 Rubies]", "6 - Crystal Heart (+20 to Max Health)[20 Rubies]", sep = "\n")


        elif cmd[0:3] == "buy":
            global inventory
            itemNumber = int(cmd[len(cmd)-1])
            avaliableRubies = inventory[1][1]

            #Buy 3 Health Pots
            if itemNumber == 1:
                cost = 15
                if avaliableRubies >= cost:
                    inventory[1][1] -= cost
                    inventory[2][1] += 3
                    print_slow ("\n3 Health Pots were added to your inventory!")
                    print_slow ( str(cost) + " Rubies deducted")
                else:
                    print_slow("Haha you have insufficient funds")

            #Buy an Iron Sabre
            if itemNumber == 2:
                cost = 30
                if avaliableRubies >= cost:
                    inventory[1][1] -= cost
                    inventory[len(inventory)-2][1] = "Iron Sabre"
                    print_slow ("\nReceived an Iron Sabre!")
                    print_slow (str(cost) + " Rubies deducted")
                else:
                    print_slow("Haha you have insufficient funds")

            #Buy Polished Armor
            if itemNumber == 3:
                cost = 30
                if avaliableRubies >= cost:
                    inventory[1][1] -= cost
                    inventory[len(inventory)-1][1] = "Polished Armor"
                    print_slow ("\nReceived some Polished Armor!")
                    print_slow (str(cost) + " Rubies deducted")
                else:
                    print_slow("Haha you have insufficient funds")

            #Buy a Void Blade  
            if itemNumber == 4:
                cost = 43
                if avaliableRubies >= cost:
                    inventory[1][1] -= cost
                    inventory[len(inventory)-2][1] = "Void Blade"
                    print_slow ("\nAttained a Void Blade!")
                    print_slow (str(cost) + " Rubies deducted")
                else:
                    print_slow("Haha you have insufficient funds")

            #Buy a Shade Cloak
            if itemNumber == 5:
                cost = 43
                if avaliableRubies >= cost:
                    inventory[1][1] -= cost
                    inventory[len(inventory)-1][1] = "Shade Cloak"
                    print_slow ("\nReceived the Shade Cloak!")
                    print_slow (str(cost) + " Rubies deducted")
                else:
                    print_slow("Haha you have insufficient funds")

            #Buy a Crystal Heart
            if itemNumber == 6:
                cost = 20
                if avaliableRubies >= cost:
                    inventory[1][1] -= cost
                    global max_hp
                    global player_hp
                    max_hp = 120
                    player_hp = 120
                    print_slow("\nConsumed the Crystal Heart!")
                    print_slow("\nMax HP increased by 20")
                    print_slow (str(cost) + " Rubies deducted")
                else:
                    print_slow("Haha you have insufficient funds")

        
        elif cmd == "quit":
            print_slow("Twas good having business with you\n")
            break

        else:
            print("INVALID COMMAND")

        
#Function to slowly print a word
def print_slow(string):
    string = string + "\n"
    for char in string:
        print(char, end='')
        time.sleep(0.00)


#A function to print the separator between commands
def line():
    print("\n===============================\n")


#A function to print the instructions
def instructions():
    print_slow("\nWelcome, brave adventurer.")
    print_slow("Your goal is to get to the end of this treacherous dungeon and collect the treasure there." + "\n")
    #time.sleep(0.25)
    print("Enemy and block index:", "A > Adventurer", "O > Old Man", "- > Blank Space", "| or ^ > Door", "# > Wall", "S > Shopkeeper", "C > Coin", "B > Bat", "T > Troll", "G > Goblin", "T > Treasure", sep = "\n", end = "\n")
    #time.sleep(5.0)
    line()


#Function to load the scene
def load_tile(scene):
    for columns in range(11):
        printableRow = ""
        for rows in range(9):
            printableRow += (scene[rows + (columns*9)]) + "  "
        print(printableRow,"\n")


#Display the inventory
def print_ineventory():
    global inventory
    line()
    for itemindex in inventory:
        iteminfo = ""
        for itemdata in itemindex:
            itemdata = str(itemdata)
            iteminfo += itemdata
        print(iteminfo)
    line()


#Gets weapon damage
def getdamage():
    global inventory
    weapon = inventory[len(inventory)-2][1]
    global weapons
    for weapondata in weapons:
        if weapondata[0] == weapon:
            return weapondata[1]


#Gets armor defense
def getdefence():
    global inventory
    armor = inventory[len(inventory)-1][1]
    global armors
    for armordata in armors:
        if armordata[0] == armor:
             return armordata[1]


#Starts a fight when the player runs into an enemy
def fight(enemy):
    global inventory
    #Determine stats of an enemy
    if enemy == "B":
        enemy_dam = 35
        enemy_hp = 50
        enemy = "Bat"
        rubies_dropped = 10
    if enemy == "G":
        enemy_dam = 45
        enemy_hp = 60
        enemy = "Goblin"
        rubies_dropped = 20
    if enemy == "T":
        enemy_dam = 60
        enemy_hp = 75
        enemy = "Troll"
        rubies_dropped = 50
    global player_hp
    player_dam = getdamage()
    player_def = getdefence()
    print_slow("\nYou approach the " + enemy + ".")
    print_slow("It starts a fight!")
    print_slow("\nType help for avaliable FIGHT commands")
    enemyWillAttack = False
    guarded = False
    #Get commands from player
    while enemy_hp > 0:
        
        #Enemy attacking
        if enemyWillAttack == True:
            
            damage_randomizer = random.randrange(-5,5)
            damage_dealt = player_dam + damage_randomizer
            defence_buffer = random.randrange(-2,2)
            damage_dealt -= (player_def + defence_buffer)

            #Effects of guarding tae place here
            if guarded == True:
                discriminant = random.randrange(0,3)
                if discriminant == 0:
                    print_slow("Your shield will absorb half the damage dealt to you")
                    damage_dealt = damage_dealt//2
                elif discriminant == 1:
                    print_slow("Your shield will negate all damage this turn")
                    damage_dealt = 0
                else:
                    print_slow("The enemy manages to somehow get past your shield. Shield Failed.")
                guarded = False
                
            player_hp -= damage_dealt
            print_slow("\nThe " + enemy + " retaliates! It hits you for " + str(damage_dealt) + " HP")
            print_slow("Your health is now " + str(player_hp))

        #Player loses if health is below 0
        if player_hp <= 0:
            global gameOver
            gameOver = [True, "Lose"]
            break


        #Get command
        cmd = str(input(">> "))


        #Help command
        if cmd == "help":
            
            print("\nAvaliable Commands:", "attack > Attack the enemy", "heal > Consume a health pot and heal 30HP", "guard > Will negate or reduce damage taken, dealing some damage to the enemy", "hp > Displays player HP", "enem_hp > Displays the enemy's hp",sep = "\n")
            time.sleep(0.5)
            line()


        #Attack command
        elif cmd == "attack":
            
            damage_randomizer = random.randrange(-5,5)
            damage_dealt = player_dam + damage_randomizer
            enemy_hp = enemy_hp - damage_dealt
            print_slow("\nYou hit the " + enemy + " for " + str(damage_dealt) + " HP.")
            print_slow("The " + enemy + "\'s HP was reduced to " + str(enemy_hp) )
            enemyWillAttack = True


        #Heal Command
        elif cmd == "heal":
            
            if inventory[2][1] > 0:
                player_hp += 30
                print_slow("Consumed a health pot and healed 30 HP")
                global max_hp
                if player_hp > max_hp:
                    player_hp = max_hp
                    print_slow("Your HP was maxed out!")
                print_slow("Your HP is now" + str(player_hp))
                enemyWillAttack = True
                
            else:
                print_slow("You do not have sufficient health pots")


        #Guard Command
        elif cmd == "guard":
            
            print_slow("You held up your trusty spiky shield and blocked the attack")
            damage_randomizer = random.randrange(-2,1)
            damage_dealt = (player_dam//6) + damage_randomizer
            enemy_hp = enemy_hp - damage_dealt
            
            print_slow("You hit the " + enemy + " for " + str(damage_dealt) + " HP.")
            print_slow("The " + enemy + "\'s HP was reduced to " + str(enemy_hp) )
            enemyWillAttack = True
            guarded = True


        #HP display commands
        elif cmd == "hp":
            print_slow("Your HP is " + str(player_hp) + "\n")


        elif cmd == "enem_hp":
            print_slow("The " + enemy + "\'s HP is " + str(enemy_hp))

            
        else:
            print("INVALID COMMAND")

    #Player defeating the enemy
    if enemy_hp <= 0:
        ruby_randomizer = random.randrange(-5,5)
        inventory[1][1] += (rubies_dropped + ruby_randomizer)
        print_slow("\nThe " + enemy + " has been defeated!")
        print_slow("You gained " + str(rubies_dropped + ruby_randomizer) + " Rubies")



#A function that handles all minor changes to the scene or effects that happen when the player interacts with another tile
def move(index,newIndex,scene):

    #Change a scene when the player runs into a door
    if scene[newIndex] == "|" or scene[newIndex] == "^":
        
        global sceneChange
        sceneChange = True
        
        scene[index] = "-"
        scene[newIndex] = "A"
        time.sleep(0.1)

    elif scene[newIndex] == "S":
        pass
        shop()

    #Add a key to player's inventory
    elif scene[newIndex] == "K":
        
        global inventory
        current_key = inventory[0][1]
        inventory[0][1] = current_key + 1
        
        print_slow("\nA key was added to your inventory!")
        print_slow(("You now have " + str(current_key + 1) + " keys"))
        
        scene[index] = "-"
        scene[newIndex] = "A"
        time.sleep(0.1)

    #Decide the dialogue of the old man
    elif scene[newIndex] == "O":
        global oldman_index
        
        if oldman_index == 0:
            print_slow("\nYou're an adventurer aren't you?")
            print_slow("\nCome to explore these dungeons?")
            print_slow("\nWell, I'm meant give you some advice before you go in so that you don't die a long, painful death.")
            print_slow("\nBefore you go in, I have to give you some advice")
            print_slow("\nBy now, you should have figured out you use commands to move and control yourself")
            print_slow("\nTry to fight monsters when you can, because they drop rubies which you can buy items with")
            print_slow("\nYou'll have to use different commands when you are fighting a monster")
            print_slow("\nJust be careful to not get brutally murdered. Good luck")

        elif oldman_index == 1:
            print_slow("\nOh hello again")
            print_slow("\nWondering how I got here? Well I won't tell you")
            print_slow("\nThere's a shop in the above room that sells useful supplies")
            print_slow("\nYou should see what they sell")
            print_slow("\nIf you don't have money, check the room below me. It's full of foul monsters")
            print_slow("\nYou should stock up on supplies before entering the room to my left. Once you enter the room on my left, you cannot turn back.")
            print_slow("\nTip: If you defeat all the enemies in a room, leaving and re-entering the room will respawn the enemies")
            print_slow("Good luck")

        elif oldman_index == 2:
            print_slow("\nSo... you made it to the end")
            print_slow("The treasure is within your reach, right in front of you")
            print_slow("At long last... I will be freed from my curse")
            print_slow("Go on, brave warrior, and take what is rightfully yours")

        scene[index] = "-"
        scene[newIndex] = "A"
        time.sleep(0.1)
        oldman_index += 1
            
    #Start a fight
    elif scene[newIndex] in enemies:
        enemy = scene[newIndex]
        fight(enemy)
        scene[index] = "-"
        scene[newIndex] = "A"
        time.sleep(0.1)

    elif scene[newIndex] == "C":
        scene[index] = "-"
        scene[newIndex] = "A"
        print_slow("\nYou open the Golden Chest")
        print_slow("\nObtained Auric Armor!")
        print_slow("\nObtained Eternity!")
        print_slow("\nObtained the Void Heart!")
        print_slow("\nConsumed the void heart! Max HP is now 9999\n")
        inventory[0][1] = 9999
        inventory[1][1] = 9999
        inventory[2][1] = 9999
        inventory[len(inventory)-2][1] = "Eternity"
        inventory[len(inventory)-1][1] = "Auric Armor"
        global max_hp
        global player_hp
        max_hp = 9999
        player_hp = 9999
        

    elif scene[newIndex] == "#":
        print_slow("You ran into a wall")
        time.sleep(0.5)

    else:
        scene[index] = "-"
        scene[newIndex] = "A"
        time.sleep(0.1)

    line()


#A function to to get a command from the user and do the approppriate action. If the user wants to move, the function move() is run
def command(scene):

    print("Type \'help\' for avaliable commands.")
    while True:
        cmd = str(input(">>>> "))
        index = scene.index("A")
        global inventory


        if cmd == "help":
            print_slow("\nCommands:")
            print("help > Display commands","inventory > View your inventory", "hp > Display player HP", "w > up","a > left","s > down","d > right","dam > Displays weapon damage", "def > Displays armor defense\n" ,sep = "\n")
            print_slow("Enemies and Tiles:")
            print("A > Adventurer", "O > Old Man", "- > Blank Space", "| or ^ > Door", "# > Wall", "S > Shopkeeper", "C > Coin", "B > Bat", "T > Troll", "G > Goblin", "C > Golden Chest", sep = "\n", end = "\n")
            time.sleep(3.0)
            line()
            break

        elif cmd == "a":
            newIndex = index-1
            scene = move(index,newIndex,scene)
            break


        elif cmd == "d":
            newIndex = index+1
            scene = move(index,newIndex,scene)
            break


        elif cmd == "w":
            newIndex = index-9
            scene = move(index,newIndex,scene)
            break


        elif cmd == "s":
            newIndex = index+9
            scene = move(index,newIndex,scene)
            break


        elif cmd == "admin":
            print_slow("Admin priviledges activated")
            inventory[0][1] = 9999
            inventory[1][1] = 9999
            inventory[2][1] = 9999
            inventory[len(inventory)-2][1] = "Eternity"
            inventory[len(inventory)-1][1] = "Auric Armor"
            global max_hp
            global player_hp
            max_hp = 9999
            player_hp = 9999


        elif cmd == "inventory":
            print_ineventory()


        elif cmd == "hp":
            print_slow("Your HP is " + str(player_hp))


        elif cmd == "dam":
            damage = getdamage()
            print("Your weapon does " + str(damage) + " damage")


        elif cmd == "def":
            defence = getdefence()
            print("Your armor gives you " + str(defence) + " defense")


        else:
            print("INVALID COMMAND")


#Strips the scene variable of all its special characters, such as keys or enemies, and returns the stripped scene for easier handling
def strip_spec_char(scene):
    global spec_chars
    index = 0
    for tile in scene:
        if tile in spec_chars:
            scene[index] = "-"
        index += 1
    return scene


#Declare the main function, a function which calls all the other main
def main():
    startRoom = [' ', '#', '#', '#', '#', '#', '#', '#', ' ',
                 '#', '#', '-', '-', '-', '-', '-', '#', '#',
                 '#', '-', '-', '-', '-', '-', '-', '-', '#',
                 '#', '-', '-', '-', '-', '-', '-', '-', '#',
                 '#', '-', '-', '-', '-', '-', '#', '-', '#',
                 '|', 'B', '-', '-', '-', '#', 'A', 'O', '#',
                 '#', '-', '-', '-', '-', '-', '#', '-', '#',
                 '#', '-', '-', '-', '-', '-', '-', '-', '#',
                 '#', '-', '-', '-', '-', '-', '-', '-', '#',
                 '#', '#', '-', '-', '-', '-', '-', '#', '#',
                 ' ', '#', '#', '#', '#', '#', '#', '#', ' ']
    instructions()
    scene = startRoom
    while gameOver[0] == False:
        newscene = []
        #Loads level
        load_tile(scene)
        #Takes input from player
        command(scene)
        global sceneChange
        #Change rooms (Hardcoded)
        if sceneChange == True:
            sceneChange = False
            #Strip special characters for easier changing of the scene
            strip_spec_char(scene)
            #First room to the junction
            if scene == [' ', '#', '#', '#', '#', '#', '#', '#', ' ',
                         '#', '#', '-', '-', '-', '-', '-', '#', '#',
                         '#', '-', '-', '-', '-', '-', '-', '-', '#',
                         '#', '-', '-', '-', '-', '-', '-', '-', '#',
                         '#', '-', '-', '-', '-', '-', '#', '-', '#',
                         'A', '-', '-', '-', '-', '#', '-', '-', '#',
                         '#', '-', '-', '-', '-', '-', '#', '-', '#',
                         '#', '-', '-', '-', '-', '-', '-', '-', '#',
                         '#', '-', '-', '-', '-', '-', '-', '-', '#',
                         '#', '#', '-', '-', '-', '-', '-', '#', '#',
                         ' ', '#', '#', '#', '#', '#', '#', '#', ' ']:
                
                scene = [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         "|", "-", "-", "-", "K", "-", "-", "A", "#",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "^", "#", " ", " ", " " ]
                print_slow("The door locks behind you...\n")

            #Junction to branch 1.1
            elif scene == [" ", " ", " ", "#", "A", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           "|", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "^", "#", " ", " ", " " ]:

                scene = ["#", "#", "#", "#", "#", "#", "#", "#", "#",
                          "#", "-", "-", "-", "-", "G", "-", "-", "#",
                          "#", "-", "-", "#", "-", "#", "-", "-", "|",
                          "#", "-", "-", "G", "-", "G", "-", "-", "#",
                          "#", "-", "-", "#", "#", "#", "#", "#", "#",
                          "#", "-", "-", "-", "-", "B", "-", "-", "#",
                          "#", "-", "-", "-", "-", "B", "-", "-", "#",
                          "#", "#", "#", "#", "#", "#", "-", "-", "#",
                          "#", "-", "-", "-", "-", "-", "-", "-", "#",
                          "#", "-", "-", "-", "A", "-", "-", "-", "#",
                          "#", "#", "#", "#", "^", "#", "#", "#", "#" ]

            #Junction to branch 2.1
            elif scene == [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           "|", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "A", "#", " ", " ", " " ]:

                scene = ["#", "#", "#", "#", "^", "#", "#", "#", "#",
                         "#", "-", "-", "-", "A", "-", "-", "-", "#",
                         "#", "-", "#", "#", "#", "#", "#", "-", "#",
                         "#", "-", "#", "-", "K", "-", "#", "-", "#",
                         "#", "-", "#", "-", "-", "-", "#", "-", "#",
                         "#", "B", "#", "-", "-", "-", "#", "B", "#",
                         "#", "-", "#", "-", "-", "-", "#", "-", "#",
                         "#", "-", "#", "-", "-", "-", "#", "-", "#",
                         "#", "-", "#", "#", "G", "#", "#", "-", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#" ]

            #Branch 1.1 to Branch 1.2
            elif scene == ["#", "#", "#", "#", "#", "#", "#", "#", "#",
                            "#", "-", "-", "-", "-", "-", "-", "-", "#",
                            "#", "-", "-", "#", "-", "#", "-", "-", "A",
                            "#", "-", "-", "-", "-", "-", "-", "-", "#",
                            "#", "-", "-", "#", "#", "#", "#", "#", "#",
                            "#", "-", "-", "-", "-", "-", "-", "-", "#",
                            "#", "-", "-", "-", "-", "-", "-", "-", "#",
                            "#", "#", "#", "#", "#", "#", "-", "-", "#",
                            "#", "-", "-", "-", "-", "-", "-", "-", "#",
                            "#", "-", "-", "-", "-", "-", "-", "-", "#",
                             "#", "#", "#", "#", "^", "#", "#", "#", "#" ]:

                scene = ["#", "#", "#", "#", " ", " ", " ", " ", " ",
                         "#", "K", "B", "#", " ", " ", " ", " ", " ",
                         "#", "B", "-", "#", " ", " ", " ", " ", " ",
                         "#", "-", "-", "#", " ", " ", " ", " ", " ",
                         "#", "-", "-", "#", " ", " ", " ", " ", " ",
                         "#", "-", "-", "#", " ", " ", " ", " ", " ",
                         "#", "-", "-", "#", " ", " ", " ", " ", " ",
                         "#", "G", "G", "#", " ", " ", " ", " ", " ",
                         "#", "-", "-", "#", " ", " ", " ", " ", " ",
                         "#", "-", "A", "#", " ", " ", " ", " ", " ",
                         "#", "#", "^", "#", " ", " ", " ", " ", " " ]

            #Branch 1.1 to junction
            elif scene == ["#", "#", "#", "#", "#", "#", "#", "#", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "#", "-", "#", "-", "-", "|",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "#", "#", "#", "#", "#", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "#", "#", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "A", "#", "#", "#", "#" ]:

                scene = [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                         " ", " ", " ", "#", "A", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         "|", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "^", "#", " ", " ", " " ]

            #Branch 1.2 to Branch 1.1
            elif scene == ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '-', '-', '#', ' ', ' ', ' ', ' ', ' ',
                           '#', '#', 'A', '#', ' ', ' ', ' ', ' ', ' ']:

                scene = ["#", "#", "#", "#", "#", "#", "#", "#", "#",
                          "#", "-", "-", "G", "-", "-", "-", "-", "#",
                          "#", "-", "-", "#", "-", "#", "-", "-", "|",
                          "#", "-", "-", "-", "-", "G", "-", "-", "#",
                          "#", "-", "-", "#", "#", "#", "#", "#", "#",
                          "#", "-", "-", "-", "-", "-", "-", "-", "#",
                          "#", "-", "-", "-", "-", "B", "-", "-", "#",
                          "#", "#", "#", "#", "#", "#", "-", "-", "#",
                          "#", "-", "-", "-", "-", "-", "-", "-", "#",
                          "#", "-", "-", "-", "A", "-", "-", "-", "#",
                          "#", "#", "#", "#", "^", "#", "#", "#", "#" ]

            #Branch 2.1 to junction
            elif scene == ["#", "#", "#", "#", "A", "#", "#", "#", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "#", "#", "#", "#", "#", "-", "#",
                           "#", "-", "#", "-", "-", "-", "#", "-", "#",
                           "#", "-", "#", "-", "-", "-", "#", "-", "#",
                           "#", "-", "#", "-", "-", "-", "#", "-", "#",
                           "#", "-", "#", "-", "-", "-", "#", "-", "#",
                           "#", "-", "#", "-", "-", "-", "#", "-", "#",
                           "#", "-", "#", "#", "-", "#", "#", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "#", "#", "#", "#", "#"]:

                scene = [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         "|", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "A", "#", " ", " ", " ",
                         " ", " ", " ", "#", "^", "#", " ", " ", " " ]

            #Junction to Junction 2. Needs 3 keys
            elif scene == [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           "A", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "^", "#", " ", " ", " " ]:
                #Consumes 3 keys
                if inventory[0][1] >= 3:
                    scene = [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                             " ", " ", " ", "#", "-", "#", " ", " ", " ",
                             " ", " ", " ", "#", "-", "#", " ", " ", " ",
                             " ", " ", "#", "#", "-", "#", " ", " ", " ",
                             "#", "#", "#", "-", "-", "#", "#", "#", "#",
                             "|", "-", "-", "-", "O", "-", "-", "A", "#",
                             "#", "#", "#", "-", "-", "#", "#", "#", "#",
                             " ", " ", "#", "#", "-", "#", " ", " ", " ",
                             " ", " ", " ", "#", "-", "#", " ", " ", " ",
                             " ", " ", " ", "#", "-", "#", " ", " ", " ",
                             " ", " ", " ", "#", "^", "#", " ", " ", " " ]
                    inventory[0][1] -= 3
                    print_slow("\nYou slid the keys into the locks")
                    print_slow("The door opens with a click")
                    print_slow("As you go through the door, it locks behing you")
                    print_slow("Again...\n")
                    
                else:
                    print_slow("\nYou examine the door...\nIt has three intricate slots in it\nYou can't seem to open it\n")

            #Junction 2 to the Shop
            elif scene == [" ", " ", " ", "#", "A", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", "#", "#", "-", "#", " ", " ", " ",
                           "#", "#", "#", "-", "-", "#", "#", "#", "#",
                           "|", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "-", "-", "#", "#", "#", "#",
                           " ", " ", "#", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "^", "#", " ", " ", " " ]:
                         
                scene = [' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ',
                         ' ', ' ', ' ', '#', 'S', '#', ' ', ' ', ' ',
                         ' ', ' ', ' ', '#', 'A', '#', ' ', ' ', ' ',
                         ' ', ' ', ' ', '#', '^', '#', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

            #Shop to Junction 2
            elif scene == [' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ',
                           ' ', ' ', ' ', '#', 'S', '#', ' ', ' ', ' ',
                           ' ', ' ', ' ', '#', '-', '#', ' ', ' ', ' ',
                           ' ', ' ', ' ', '#', 'A', '#', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
                
                scene = [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                         " ", " ", " ", "#", "A", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", "#", "#", "-", "#", " ", " ", " ",
                         "#", "#", "#", "-", "-", "#", "#", "#", "#",
                         "|", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "#", "-", "-", "#", "#", "#", "#",
                         " ", " ", "#", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "^", "#", " ", " ", " " ]
                
            #Junction 2 to Mob Farm Area
            elif scene == [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", "#", "#", "-", "#", " ", " ", " ",
                           "#", "#", "#", "-", "-", "#", "#", "#", "#",
                           "|", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "-", "-", "#", "#", "#", "#",
                           " ", " ", "#", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "A", "#", " ", " ", " " ]:
                
                scene = [" ", " ", "#", "#", "^", "#", "#", " ", " ",
                         " ", " ", "#", "-", "A", "-", "#", " ", " ",
                         "#", "#", "#", "-", "-", "-", "#", "#", "#",
                         "#", "-", "B", "-", "-", "-", "G", "-", "#",
                         "#", "G", "-", "-", "-", "-", "-", "B", "#",
                         "#", "-", "B", "-", "-", "-", "G", "-", "#",
                         "#", "G", "-", "-", "-", "-", "-", "B", "#",
                         "#", "-", "B", "-", "-", "-", "G", "-", "#",
                         "#", "#", "#", "#", "-", "#", "#", "#", "#",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "#", "#", " ", " ", " " ]
                    
            #Mob Farm Area to junction
            elif scene == [" ", " ", "#", "#", "A", "#", "#", " ", " ",
                           " ", " ", "#", "-", "-", "-", "#", " ", " ",
                           "#", "#", "#", "-", "-", "-", "#", "#", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "-", "#", "#", "#", "#",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "#", "#", " ", " ", " " ]:
                
                scene = [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", "#", "#", "-", "#", " ", " ", " ",
                         "#", "#", "#", "-", "-", "#", "#", "#", "#",
                         "|", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "#", "-", "-", "#", "#", "#", "#",
                         " ", " ", "#", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "-", "#", " ", " ", " ",
                         " ", " ", " ", "#", "A", "#", " ", " ", " ",
                         " ", " ", " ", "#", "^", "#", " ", " ", " " ]

            #Junction 2 to Final Corridor
            elif scene == [" ", " ", " ", "#", "^", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", "#", "#", "-", "#", " ", " ", " ",
                           "#", "#", "#", "-", "-", "#", "#", "#", "#",
                           "A", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "-", "-", "#", "#", "#", "#",
                           " ", " ", "#", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "-", "#", " ", " ", " ",
                           " ", " ", " ", "#", "^", "#", " ", " ", " " ]:
                
                scene = [" ", " ", " ", " ", " ", " ", " ", " ", " ",
                         " ", " ", " ", " ", " ", " ", " ", " ", " ",
                         " ", " ", " ", " ", " ", " ", " ", " ", " ",
                         " ", " ", " ", " ", " ", " ", " ", " ", " ",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "|", "-", "T", "-", "T", "-", "T", "A", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         " ", " ", " ", " ", " ", " ", " ", " ", " ",
                         " ", " ", " ", " ", " ", " ", " ", " ", " ",
                         " ", " ", " ", " ", " ", " ", " ", " ", " ",
                         " ", " ", " ", " ", " ", " ", " ", " ", " " ]
                print_slow("The door locks behind you\nThis is the final stretch")
                
            #Final Corridor to treasure room
            elif scene == [" ", " ", " ", " ", " ", " ", " ", " ", " ",
                           " ", " ", " ", " ", " ", " ", " ", " ", " ",
                           " ", " ", " ", " ", " ", " ", " ", " ", " ",
                           " ", " ", " ", " ", " ", " ", " ", " ", " ",
                           "#", "#", "#", "#", "#", "#", "#", "#", "#",
                           "A", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "#", "#", "#", "#", "#",
                           " ", " ", " ", " ", " ", " ", " ", " ", " ",
                           " ", " ", " ", " ", " ", " ", " ", " ", " ",
                           " ", " ", " ", " ", " ", " ", " ", " ", " ",
                           " ", " ", " ", " ", " ", " ", " ", " ", " " ]:
                
                scene = ["#", "#", "-", "-", "-", "-", "-", "#", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "#", "#", "-", "-", "#", "#", "#",
                         "|", "-", "-", "-", "C", "-", "O", "A", "#",
                         "#", "#", "#", "#", "-", "-", "#", "#", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "-", "-", "-", "-", "-", "-", "-", "#",
                         "#", "#", "-", "-", "-", "-", "-", "#", "#" ]
                
            #Treasure Room to Exit Corridor
            elif scene == ["#", "#", "-", "-", "-", "-", "-", "#", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "-", "-", "#", "#", "#",
                           "A", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "#", "#", "-", "-", "#", "#", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "-", "-", "-", "-", "-", "-", "-", "#",
                           "#", "#", "-", "-", "-", "-", "-", "#", "#" ]:
                scene = ["-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", "#", "#", "#", "#", "#", "#", "#",
                         "-", "|", "T", "T", "T", "T", "T", "A", "#",
                         "-", "#", "#", "#", "#", "#", "#", "#", "#",
                         "-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", " ", " ", " ", " ", " ", " ", " ",
                         "-", "#", " ", " ", " ", " ", " ", " ", " " ]
            #Game win
            else:
                gameOver[0] = True
                gameOver[1] = "Win"

    #What happens when the game ends
    if gameOver[1] == "Lose":
        print_slow("You died a painful death")
        print_slow("You should have never gone into the dungeon")
    if gameOver[1] == "Win":
        print_slow("You escaped the dungeon with your new sword and armor")
        print_slow("You are revered in all lands as the greatest warrior alive")
        print_slow("Good job!\n")

    gameStopped = False
    #Ask whether the player wants to play again
    while gameStopped == False:
        option = str(input("Would you like to play again? [y/n]: "))
        if option == "y":
            #reset()
            main()
        else:
            print_slow("Thank you for playing. Bai")
            gameStopped = True

#Run the looping main function
main()



