# import necessary modules.
from os import path, remove
from base64 import urlsafe_b64encode, urlsafe_b64decode
from string import ascii_letters
from io import UnsupportedOperation
import shelve
import time
import sys
import random
import pickle

# create the filesystem file
fs = shelve.open('filesystem.fs', writeback=True)

# =============================================================================
# Functions used in the game
# =============================================================================

def openCred():
    # opens the saved pickled file with the encrypted key and password
    
    global key, encryptedPass

    try:
        with open('credential.ini','rb') as credFile:
            cred=pickle.load(credFile)
            # decrypt and save the content into the various variables
            key=decrypt("PorridgePi",cred["key"])
            encryptedPass=cred["rootpw"]
        
        # return that the key and the encrypted password is successfully obtained
        return True

    # except UnpicklingError - damaged file, EOFError - empty file
    # and FileNotFoundError - missing file
    except (pickle.UnpicklingError,EOFError,FileNotFoundError):

        # return that an error has occurred and a new game will be started
        return False

def saveCred():
    # save the current key and password into a file

    with open('credential.ini','wb') as credFile:
        # encrypt the key for security
        encryptedKey=encrypt('PorridgePi',key)

        # save the key and the password as a dictionary and pickle it into a file
        cred={"key":encryptedKey,"rootpw":encryptedPass}
        pickle.dump(cred,credFile)

    credFile.close()

def delay_print(s):
    # a function to print character by character

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def dupList(list):
    # duplicate a list manually instead of a=b 
    # because when a=b, the changes of a and b are "synced"

    result=[]

    for i in list:
        result.append(i)

    return result

def tooArgs(arg):
    # shows an error that there are too many arguments for a command

    print("-bash: "+arg+": too many arguments")

def encrypt(k,s):
    # a function to encrypt the given string with a given key

    encryptedChars = []

    for i in range(len(s)):
        key_c=k[i%len(k)]
        encryptedChar=chr(ord(s[i])+ord(key_c)%256)
        encryptedChars.append(encryptedChar)
    encryptedStr="".join(encryptedChars)
    
    # returns a byte
    return urlsafe_b64encode(encryptedStr.encode())

def decrypt(k,s):
    # decrypt a given byte with a given key and returns a string

    s=urlsafe_b64decode(s).decode()
    decryptedChars = []
    for i in range(len(s)):
        key_c=k[i%len(k)]
        decryptedChar=chr(ord(s[i])-ord(key_c)%256)
        decryptedChars.append(decryptedChar)
    decryptedStr="".join(decryptedChars)
    
    # returns the decrypted string
    return decryptedStr

def genPass(a=8,b=16):
    # generate a random string with length ranging from 8 to 16

    letters=ascii_letters
    passList=[]
    for i in range(random.randint(a,b)):

        # appends a random letter to the list
        passList.append(random.choice(letters))
    
    # join all items in the list into one string

    password="".join(passList)

    # returns the generated random string
    return password

# =============================================================================
# Key Commands used in the Linux OS
# =============================================================================

def currentDict():
    # return a dictionary representing the files in the current directory
    # used by other commands to:
        # check if a file/folder is present
        # list files/folders in current directory
    
    d = fs[""]
    for i in currentDir:
        d = d[i]

    # a dictionary is returned
    return d

def ls(args):
    # lists the files/folders present in the current directory
    print ('Contents of directory', "/" + "/".join(currentDir) + ':')
    for i in currentDict():
        print(i)

def cd(args,integrate=False):
    # changes (current) directory

    # make the variable global so the changes are valid
    global currentDir

    if len(args)<1:
        # if no argument or path is provided, stop immediately
        return
    
    elif len(args)>=2:
        # if too many argumets are provided, show an error
        tooArgs("cd")
    
    elif args[0] == "..":
        # return to the previous directory
        if len(currentDir) == 0:
            print ("Cannot go above root")
        else:
            currentDir.pop()
    
    else:
        # a valid path was provided and change the directory

        # root refers to whether the path contains / or it starts from the root
        root=False
        
        if args[0]=="/":
            # returns to the root filesystem at / and exit

            currentDir=[]
            return 
        
        elif args[0][0]=="/":
            # if a path in the format /a/b was provided, split the path into a list
            root=True
            org=args[0]
            args=args[0].split("/")

        elif args[0]=="~":
            # goes to the home folder and exit if only ~ is provided

            currentDir=["home",username]
            return
            
        elif args[0][0]=="~":
            if args[0][1]!="/":
                if args[0][1]=="~":
                    # if the path entered starts with ~~, split the path and
                    # enter the directory later using the main function

                    if "/" in args[0]:
                        args=args[0].split("/")

                else:
                    # shows an error that directory does not exist as it is not possible to have
                    # directories starting with only 1 ~
                    print("bash: no such user or named directory: "+args[0][1:])

                    # exit the function
                    return
            else:
                # if path given is contains / then split and store the path given
                # and change the directory with the main function below
                args[0]="/home/"+username+args[0][1:]
                org=args[0]
                args=args[0].split("/")

        elif "/" in args[0]:
            # if the path given contains / then split and store the path given
            # and change the directory with the main function below
            
            if currentDir!=[]:
                # if the current directory is not at, then add an additional "/"
                org="/"+"/".join(currentDir)+"/"+args[0]

            else:
                org="/"+args[0]

            args=args[0].split("/") 
            


        if len(args)>1:
            # the argument is a long path (such as /home/abc/d)

            # save the current directory so as to return to it if the directory is not found
            org_dir=currentDir
            
            # if the path starts with /, then set the current directory to root (/) 
            # so as to facilitate with the changing of the directory later
            if root:
                currentDir=[]

            for i in args:
                # iterate through each of the path given one by one

                if i=="":
                    # ignore if the path is "", this happens when I split a text like "/"
                    # it will be split into ["",""]
                    continue

                elif i not in currentDict():
                    # show an error
                    if not integrate:
                        # show error that the direcory is not found if this command is not used by other commands
                        print ("Directory "+org+" not found")

                    else:
                        # return an error to the command using this command
                        return "notFound"
                    
                    # returns to the original directory before the player tried to change directory
                    currentDir=org_dir

                    # end the loop and exit
                    break

                elif type(currentDict()[i])==dict:
                    if currentDir==[] and i in PROTECTED:  
                        # check if the directory is protected

                        if not ELEVATED:
                            # if the user try to change directory into a protected directory without elevation, show an error
                            print("cd: cannot change directory: Permission denied")

                        elif ELEVATED:
                            # change the directory if privilege is elevated
                            currentDir.append(i)

                    else:
                        # if the directory is not protected, then change current directory to it
                        currentDir.append(i)

                elif type(currentDict()[i])!=dict:
                    # show/return an error if the directory entered is not a directory
                    if not integrate:
                        print("-bash: cd: "+org+": Not a directory")
                    else:
                        return "notDir"

                    # returns to the original directory before the player tried to change directory    
                    currentDir=org_dir
                    break

        else:
            # there is only 1 path provided

            if args[0] not in currentDict():
                # show/return an error if the directory entered does not exist
                if not integrate:
                    print ("Directory " +"/"+"/".join(currentDir)+"/"+args[0] + " not found")
                else:
                    return "notFound"

            elif type(currentDict()[args[0]])==dict:
                if currentDir==[] and args[0] in PROTECTED:
                    # check if the folder is protected

                    if not ELEVATED:
                        # if the user try to change directory into a protected directory without elevation, show an error
                        print("cd: cannot change directory: Permission denied")

                    elif ELEVATED:
                        # change the directory if privilege is elevated
                        currentDir.append(args[0])

                else:
                    currentDir.append(args[0])

            elif type(currentDict()[args[0]])!=dict:
                # show/return an error if the directory entered is not a directory
                if not integrate:
                    print("-bash: cd: "+"/"+"/".join(currentDir)+"/"+args[0]+": Not a directory")
                else:
                    return "notDir"

def cat(args):
    # a function to view the contents in a file

    if len(args)<1:
        # exit if no filename is provided
        return
        
    else:
        for i in args:
            # iterate through the files provided
            
            if i not in currentDict():
                # show error if file is not found
                print ("cat: "+i+": No such file or directory")

            elif i == ".." or type(currentDict()[i])==dict:
                # show error if file is a directory
                print("cat: "+i+": Is a directory")

            elif type(currentDict()[i])!=dict:
                # shows the contents of the file
                print(currentDict()[i])

def mkdir(args):
    # function to create an empty directory

    global currentDir

    if len(args) < 1:
        # shows error if no argument is provided
        print ("Usage: mkdir [directory]")
        return
    
    elif len(args)>=2:
        # shows error if too many argumment is provided
        tooArgs("mkdir")
    
    elif "/" in args[0]:
        # if / in the argument, split the string into a list and slowly cd into it
        originalDir=dupList(currentDir)
        origDir=args[0].split("/")
        toAdd=origDir[-1]
        origDir.pop()
        origDir=["/"+"/".join(origDir)]
        cd(origDir,True)
        
        # try to check if the directory already exists
        try:
            if type(currentDict()[toAdd])!=dict:
                # when the directory does not exist, create an empty temporary directory
                temp=currentDict()[toAdd]={}

            else:
                # show error if directory exists
                print("Directory exists!")
            currentDir=originalDir

        except KeyError:
            # when the directory does not exist, create an empty temporary directory
            temp=currentDict()[toAdd]={}
    
    else:
        # only 1 argument is provided 
        try:
            if type(currentDict()[args[0]])!=dict:
                # when the directory does not exist, create an empty temporary directory
                temp=currentDict()[args[0]]={}

            else:
                # show error that the directory exist
                print("Directory exists!")

        except KeyError:
            # when the directory does not exist, create an empty temporary directory
            temp=currentDict()[args[0]]={}
    
    # sync the changes
    fs.sync()

def rm(args):
    # function to remove a file or a directory (only when -r recursive is used)

    global currentDir

    # recursive is False originally unless stated
    recursive=False
    
    # creates empty list for the list of options to be removed from the arguments
    toPop=[]

    if len(args)<1:
        # show error and exit if no argument is provided
        print("rm: missing operand")
        print("Usage: rm [OPTION]... [FILE]...\n  -r    remove directories and their contents recursively")
        return

    for i in range(len(args)):
        item=args[i]
        # iterate through the arguments

        if item[0]=="-":
            # if the item starts with - , check if the option is -r

            options=item.split("-")[-1]

            for option in options:
                if option!="r":
                    # show error if invalid option is provided

                    print("rm: invalid option -- '"+option+"'")
                    return

                elif option=="r":
                    # if -r option is provided, recursive will be set to True

                    recursive=True

                    if i not in toPop:
                        # add to the list of options to be removed from the arguments
                        toPop.append(i)

    for i in range(len(toPop)):
        # remove the option from the list of arguments
        args.pop(toPop[i]-i)

    for arg in args:
        # iterate through each argument in the arguments provided               
        if "/" in arg:
            
            originalDir=dupList(currentDir)
            origDir=arg.split("/")
            toRm=origDir[-1]
            origDir.pop()
            origDir=["/"+"/".join(origDir)]
            temp=cd(origDir,True)

            try:
                if type(currentDict()[toRm])!=dict:
                    currentDict().pop(toRm)

                else:
                    if recursive:
                        if currentDir==[] and toRm in PROTECTED:
                            if not ELEVATED:
                                print("rm: cannot remove '"+arg+"': Permission denied")
                            else:
                                currentDict().pop(toRm)
                        else:
                            currentDict().pop(toRm)
                    else:
                        print("rm: cannot remove '"+arg+"': Is a directory")
                currentDir=originalDir

            except KeyError:
                print("rm: cannot remove '"+arg+"': No such file or directory")
        else:
            try:
                if type(currentDict()[arg])!=dict:
                    temp=currentDict().pop(arg)
                else:
                    if recursive:
                        if currentDir==[] and arg in PROTECTED:
                            if not ELEVATED:
                                print("rm: cannot remove '"+arg+"': Permission denied")
                            else:
                                currentDict().pop(arg)
                        else:
                            currentDict().pop(arg)
                    else:
                        print("rm: cannot remove '"+arg+"': Is a directory")
            except KeyError:
                print("rm: cannot remove '"+arg+"': No such file or directory")

def sudo(args):
    global ELEVATED
    ELEVATED=False
    numTry=1
    pw=""
    try:
        pw=input("[sudo] password for "+username+": ")
        for i in range(1,3):
            if pw!=decrypt(key,encryptedPass):
                numTry+=1
                pw=input("[sudo] password for "+username+": ")
            else:
                numTry=0
                break
            
    except KeyboardInterrupt:
        pass
    
    try:
        if pw==decrypt(key,encryptedPass) and len(args)>0:
            ELEVATED=True
            inputRun(args)
        elif numTry==1:
            print("\nsudo: "+str(numTry)+" incorrect password attempt")
        elif numTry==2:
            print("\nsudo: "+str(numTry)+" incorrect password attempts")
        elif numTry==3:
            print("sudo: "+str(numTry)+" incorrect password attempts")

    except RuntimeError:
        raise RuntimeError

def userHelp(args):
    # prints the help message
    print(helpMsg)

# =============================================================================
# All Key Linux commands are defined.
# =============================================================================

# =============================================================================
# Functions used in the playing of the game
# =============================================================================

def retrievePass(args):
    # function to decrypt password from the given key and encrypted password
    choice=input("This command does NOT find the password for you.\nInstead, it helps you to decrypt the password \nusing the encrypted password and the key, which you need to find.\nDo you understand? (y/n)\n>>>")
    
    if choice == "y":
        pw=input("Please enter the encrypted password that you found.\n>>> ")
        key=input("Please enter the key that you found.\n>>>")

        try:
            # decrypt and print decrypted password
            rootpw=decrypt(key,pw.encode())
            print("Here is the root password decrypted from the information you provided.\n"+rootpw)

        except IndentationError:
            # password cannot be decrypted
            # show error
            print("Seems like you got the wrong key or password. Try again!")

def genAccount():
    # creates the user and initialise the filesystem

    global username, encryptedPass, key, currentDir
    
    # generate the key and the password
    key=genPass(10,10)
    rootpass=genPass()
    
    # generate the encrypted password
    encryptedPass=encrypt(key,rootpass)
    
    done=False
    num=["1","2","3","4","5","6","7","8","9","0"]

    while not done:
        # repeat asking for username until the username is acceptable
        username = input('What do you want your username to be? ')
        
        if " " in username:
            # make sure that the username does not contain any spaces
            print("Your username should not contain spaces.")
        
        elif username[0] in num:
            # make sure that the username does not begin with a number
            print("Your username should not begin with a number.")
        
        else:
            done=True
            break
    
    # initialize the filesystem structure and files.
    fs[""] = {
            "bin":{"a":{}},
            "boot":{},
            "dev":{},
            "etc":{},
            "home":{username: {"help.txt":helpMsg},
                    "Prof": {"backup.txt":encryptedPass.decode()}},
            "lib":{},
            "opt":{},
            "sbin":{},
            "srv":{},
            "tmp":{},
            "usr":{}
            }

    # set the current directory to the home directory of the player
    currentDir=["home",username]

    # welcome message
    welcomeMsg = "\nWelcome back, Agent "+username+"""!

You are back on another mission.

Your goal today is to hack this computer, which is running Linux.
By deleting the /bin folder on this computer, everything will stop fuctioning properly.
Therefore, you just need to delete the /bin folder.

However, no matter what you do, you must find the root password.

According to our intelligence, the owner saved a copy of his password in his personal home folder.
However, it is encrypted.

Our intelligence also discovered that the owner enjoyed making text-based RPG games.
We could not guarantee but there may be clues to decrypt the password in the game.

To make it easier for you, we had included a copy of his game in your account.
You can play the game by entering the command: playgame.

We had also included a copy of our specialised decrypter.
After finding the key and the encrypted password, you can use it to decrypt the final root password. 
You can use it by entering the command: retrievepass

Since this computer is running Linux, you need to know the Linux syntax.
You can find more information and help about the basic syntax by entering the commmand: help.

That's all. All the best!\n
"""

    # print the welcome message character by character
    delay_print(welcomeMsg)   

def init(fs):
    # initialization:
    # open files and create users, passwords and initialize filesystem
    
    global username, currentDir
    
    username="" 
    # resets the username

    try:
        # checks if there was a previous game saved as a file
        
        if type(fs[""])==dict and openCred():
        # checks if the file saved was not "corrupted"
            
            if not DEBUG:
                saved=input("Did you save your previous game? (y/n) >>> ")
                # ask player if he/she was the one played the previous game

            else:
                saved="y"
            
            if saved.lower()=="y":
                if not DEBUG:
                    uname=input("Input your username >>> ")
                else:
                    uname="l"
                
                if uname in fs[""]["home"]:
                    # check if the username inputted was the username saved in the file
                    # username is found in the file, so set the username and welcome bacl

                    print("Welcome back, "+uname+".")
                    username=uname
                    currentDir=["home",username]

                else:
                    # username entered does not match the one in the file saved 
                    # creates a new game

                    print("Wrong username.\nStarting new game.")
        else:
            # if type of the filesystem is not a dictionary or the credentials saved cannot be found
            # conclude that something is currupted and start a new game
            print("Saved game is currupted.\nStarting new game.")

        if username=="":
            # if the username did not change, then create a new account
            genAccount()
    
    except KeyError:
        # if no file saved, then create a new game 
        genAccount()
    
    except (pickle.UnpicklingError, EOFError):
        # something is currupted or the file is empty
        # start a new game
        print("Saved game is currupted.\nStarting new game.")
        genAccount()


def exitProgram(args):
    # a function to raise an error, allowing the game to end
    raise RuntimeError

def inputRun(raw):
    # a function that splits input text and start the function to do it 
    # with the given arguments

    if type(raw)==str:
        # if the input data is a string, then split it using spaces
        fullCmd=raw.split()

    elif type(raw)==list:
        # if the input data is a list, then pass
        fullCmd=raw

    if len(fullCmd)>0:
        # set the main function to be called
        cmd=fullCmd[0]

    else:
        # since nothing is inputted, exit
        return

    if cmd in COMMANDS:
        try:
            COMMANDS[cmd](fullCmd[1:])

        except RuntimeError:
            # I used RuntimeError to end the entire program
            # if a function raises RuntimeError, it will be repeated, and the main loop will break
            raise RuntimeError
    else:
        # show error if command is not present
        print(cmd+": command not found")

def checkWin():
    # check if the player has won by deleting the /bin folder
    if "bin" not in fs[""]:
        print("You have successfully hacked this computer.\nIt is now broken.\nTherefore, you completed your task.\nIn short, YOU WON!\n")
        exitProgram(0)

# =============================================================================
# RPG Game which allows the player to find the key to decrypt the password
# =============================================================================

def game(args):
    def inputRun(raw):
        # a function that splits input text and start the function to do it 
        # with the given arguments
        fullCmd=raw.split()
        
        if len(fullCmd)>0:
            cmd=fullCmd[0]
        else:
            return
        
        if cmd in GAMECMDS:
            try:
                GAMECMDS[cmd](fullCmd[1:])
            except RuntimeError:
                raise RuntimeError
        else:
            print(cmd+": command not found")
            
    def printMsg(short=False):
        if not short:
            if currentLoc=="beach":
                print("You arrived at the beach.")
            else:
                print("You entered the "+currentLoc+".")
        else:
            print("You looked around.")
        
        msgs={
        "beach":"You saw something stuck into the sand.",
        "forest":"You saw a thing hanging down from the tree.",
        "house":"There was nothing in the house.",
        "cave":"You saw a gigantic cross on the floor."
        }
        
        print(msgs[currentLoc])

    def help(args):
        helpMsg="""You goal is to find the key. 
Possible Commands:
        go [location]   => to go to a location
        kill [creature] => to kill a creature, including yourself!
                           (Maybe try killing yourself?)
        exit            => to exit the game
        see             => to look around
        find [item]     => to find an item
        help            => to view this help
        """
        print(helpMsg)

    def go(args):
        global currentLoc
        if len(args)>= 1 and args[0] in locs and len(args)==1:
            currentLoc=args[0]
            printMsg()

        elif len(args)==1:
            print("ERROR: Location not found")

        else:
            print("ERROR: Too many arguments!")
    
    def kill(args):

        if len(args)>=1:
            if args[0]=="me" or args[0]=="myself":
                print("\nYou killed yourself. You died!")
                if keyFound:
                    print("However, you found the key of the value "+key+".")
                endGame(0)

            else:
                print(" ".join(args)+" not found!")
    
    def endGame(args):
        global end
        if not keyFound:
            print("Bye!")

        else:
            print("You technically won the game! Goodbye!")

        end=True

    def see(args):
        printMsg(True)
    
    def find(args):
        global keyFound
        
        if len(args)>= 1 and args[0]=="key":

            if currentLoc=="beach":
                print("You took a closer look at the thing in the sand.")

            elif currentLoc=="house":
                print("You walked around the house.")
                print("There was a tiny hole on the ground.")
                print("You peeked into it and saw something.")

            elif currentLoc=="forest":
                print("You took a closer look at the thing hanging down from the tree.")

            elif currentLoc=="cave":
                print("You decided to dig a hole at the location of the cross.")
            
            time.sleep(2)

            if currentLoc==keyLoc:
                if currentLoc=="cave":
                    print("Something appeared.")

                keyFound=True
                print("It was shiny and brown in colour.")
                print("CONGRATULATION! You found the key!")

            else:
                if currentLoc=="beach":
                    print("It was just a twig.")

                elif currentLoc=="house":
                    print("You realised that it was simply an ant.")

                elif currentLoc=="forest":
                    print("It was just a spider.")

                elif currentLoc=="cave":
                    print("There was nothing.")

        else:
            print(" ".join(args)+" not recognised!")

    global currentLoc, end, keyFound, keyLoc, locs

    locs=["beach","forest","house","cave"]
    keyLoc=random.choice(locs)
    keyFound=False
    end=False
    currentLoc="house"
    GAMECMDS={"go":go,"help":help,"kill":kill,"see":see,"exit":endGame,"find":find} 
    
    print("""Welcome to the game, adventurer. \n
You found a treasure box on this island, but you could not find the key to open it yet.\n
There are four locations on this island, namely the beach, forest, house and the cave.\n
Your goal is to find the key.\n
You can move around by entering: go [location]
There may be creatures on this island that will attack you.
You can defend yourself by killing the creature using the command: kill [creature]\n
After finding the key, you can continue to explore the island, or exit the game.\n
To view help, you can enter: help.\n
Have fun!\n
    """)
    print("You are in the house.")
    
    while not end:
        try:
            raw=input("\n>>> ")
            print("")
            inputRun(raw.lower())
        except KeyboardInterrupt:
            end=True
        
global helpMsg

# resets the current directory for the player
currentDir = []

# Define commands
COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir, "sudo":sudo, "exit":exitProgram,
            "cat":cat, "help":userHelp, "playgame":game,"rm":rm,"retrievepass":retrievePass}

PROTECTED = {
            "bin":{},
            "boot":{},
            "dev":{},
            "etc":{},
            "lib":{},
            "opt":{},
            "sbin":{},
            "srv":{},
            "tmp":{},
            "usr":{}
}

helpMsg="""
These are the in-game commands and aliases:

>>  help
        views this help
>>  exit
        exits the game
>>  retrievepass
        opens the decrypter to decrypt the password
>>  playgame
        plays the game made by the owner of this computer

The following are usage of the basic commands in Linux and its functions:

>>  ls  
        lists the files and directories present in the current directory
>>  cd
        change directory
    Usage:
        cd [DIRECTORY or PATH]
        cd ..
            goes to the previous directory
>>  mkdir
        make directory (a.k.a. folder)
    Usage:
        mkdir [DIRECTORY or PATH]
>>  sudo
        run command with elevated privileges 
    Usage:
        sudo [COMMAND] ...
>>  cat
        views the contet of file(s)
    Usage:
        cat [FILE]
>>  rm
        removes file or directory
    Usage: 
        rm [OPTION]... [FILE]...
        OPTION:
            -r  remove directories and their contents recursively
                (used to remove directories)
    """

# sets the state of DEBUG 
DEBUG=False

# Initialization
init(fs)

while True:
    try:
        # sync the data at all time
        fs.sync()
        saveCred()

        # check if the player win
        checkWin()

        # set the elevation to False unless sudo is used
        ELEVATED=False

        if len(currentDir)>=2:
            if currentDir[0]=="home" and currentDir[1]==username:
                if len(currentDir)==2:
                    # when the player is in his home directory, print ~ instead
                    raw = input(username+"@"+"ThinkPadX1C:~ $ ")
                    
                elif len(currentDir)>=2:
                    # when the player is in his home directory, print path starting with ~ instead
                    homeDir=dupList(currentDir)[2:]
                    raw = input(username+"@"+"ThinkPadX1C:~/"+"/".join(homeDir)+" $ ")

            else:
                # print the path 
                raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(currentDir)+" $ ")

        else:
            # print the path 
            raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(currentDir)+" $ ")

        # run the command obtained
        inputRun(raw)

    except RuntimeError:
        # break and stop the program upon receieving RuntimeError
        break

save=input("Game stopped. Do you want to save the game? (y/n) >>> ")
if save.lower()=="y":
    fs.sync()
    saveCred()
    input('Game saved. Press the Enter key to shutdown...')
else:
    # close the file used by shelves
    fs.close()

    # Removes the files saved by shelves and pickle
    if path.exists("filesystem.fs.dir"):
        remove("filesystem.fs.dir")
    if path.exists("filesystem.fs.dat"):
        remove("filesystem.fs.dat")
    if path.exists("filesystem.fs.bak"):
        remove("filesystem.fs.bak")
    if path.exists("credential.ini"):
        remove("credential.ini")

    input('Game NOT saved. Press the Enter key to shutdown...')
