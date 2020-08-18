import shelve
import os
import time
import sys

DEBUG=True
VERBOSE=False
# create the filesystem file
fs = shelve.open('filesystem.fs', writeback=True)\

# resets the current directory for the player
currentDir = []
def verbose():
    if VERBOSE:
        print(currentDir,currentDict())


def delay_print(s):
    # a function to print character by character
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def dupList(list):
    # duplicate a list manually instead of a=b 
    # because when a=b, the changes of a and b are "synced"
    result=[]
    for i in list:
        result.append(i)
    return result

def tooArgs(arg):
    # alert that there are too many arguments for a command
    print("-bash: "+arg+": too many arguments")

def genAccount():
    # creates the user and initialise the filesystem
    global username
    done=False
    num=["1","2","3","4","5","6","7","8","9","0"]

    while not done:
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
            "bin":{},
            "boot":{},
            "dev":{},
            "etc":{},
            "home":{username: {"help.txt":"This is help"}},
            "lib":{},
            "opt":{},
            "sbin":{},
            "srv":{},
            "tmp":{},
            "usr":{}
            }

    # welcome message
    welcomeMsg = """Welcome, hacker!
You are back on another mission.
Your goal today is to hack this computer, which is running Linux.
No matter what you do, you must find the root password.
There are 3 ways of doing so:
    1. Find and use the Brute-Force password hacker.
    2. Find the password encrypted in the file system using clues.
    3. Find the password that the owner had kept as a text file.
"""

    # print the welcome message character by character
    delay_print(welcomeMsg)   


def init(fs):
    # create users, passwords and initialize filesystem
    global username, rootpass
    rootpass="poop" # the root password that the player should find at last
    username="" # resets the username
    
    try:
    # checks if there was a previous game saved as a file
        
        if type(fs[""])==dict:
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
                # check if the username inputted was the username saved in the file
                if uname in fs[""]["home"]:
                    print("Welcome back, "+uname+".")
                    username=uname
        
        if username=="":
            # if the username did not change, then create a new account
            genAccount()
    
    except:
    # if no file saved, then create a new account 
        genAccount()

# =============================================================================
# Key Commands in Linux
# =============================================================================

def currentDict():
    # return a dictionary representing the files in the current directory
    # used by other commands to:
        # check if a file/folder is present
        # list files/folders in current directory
    
    d = fs[""]
    for i in currentDir:
        d = d[i]
    return d

def ls(args):
    # lists the files/folders present in the current directory
    print ('Contents of directory', "/" + "/".join(currentDir) + ':')
    for i in currentDict():
        print(i)

def cd(args,integrate=False):
    # changes (current) directory
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
        root=False
        # a valid path was provided and change the directory
        if args[0]=="/":
            currentDir=[]
            return 
        
        elif args[0][0]=="/":
            # if a path in the format /a/b was provided, split the path into a list
            root=True
            org=args[0]
            args=args[0].split("/")

        elif args[0]=="~":
            currentDir=["home",username]
            return
            
        elif args[0][0]=="~":
            if args[0][1]!="/":
                if args[0][1]=="~":
                    if "/" in args[0]:
                        args=args[0].split("/")         
                else:
                    print("bash: no such user or named directory: "+args[0][1:])
                    return
            else:
                args[0]="/home/"+username+args[0][1:]
                org=args[0]
                args=args[0].split("/")

        elif "/" in args[0]:
            if currentDir!=[]:
                org="/"+"/".join(currentDir)+"/"+args[0]
            else:
                org="/"+args[0]
            args=args[0].split("/") 
            


        if len(args)>1:
            org_dir=currentDir
            if root:
                currentDir=[]
            for i in args:
                if i=="":
                    continue
                elif i not in currentDict():
                    if not integrate:
                        print ("Directory "+org+" not found")
                    else:
                        return "notFound"
                    currentDir=org_dir
                    break
                elif type(currentDict()[i])==dict:
                    currentDir.append(i)
                elif type(currentDict()[i])!=dict:
                    if not integrate:
                        print("-bash: cd: "+org+": Not a directory")
                    else:
                        return "notDir"
                    currentDir=org_dir
                    break
        else:
            if args[0] not in currentDict():
                if not integrate:
                    print ("Directory " +"/"+"/".join(currentDir)+"/"+args[0] + " not found")
                else:
                    return "notFound"
            elif type(currentDict()[args[0]])==dict:
                currentDir.append(args[0])
            elif type(currentDict()[args[0]])!=dict:
                if not integrate:
                    print("-bash: cd: "+"/"+"/".join(currentDir)+"/"+args[0]+": Not a directory")
                else:
                    return "notDir"
def cat(args):
    if len(args)<1:
        return
    else:
        for i in args:    
            if i not in currentDict():
                print ("cat: "+i+": No such file or directory")
            elif i == ".." or type(currentDict()[i])==dict:
                print("cat: "+i+": Is a directory")
            elif type(currentDict()[i])!=dict:
                print(currentDict()[i])

def mkdir(args):
    global currentDir
    if len(args) != 1:
        print ("Usage: mkdir <directory>")
        return
    # create an empty temporary directory there and sync back to shelve dictionary!
    if "/" in args[0]:
        originalDir=dupList(currentDir)
        origDir=args[0].split("/")
        toAdd=origDir[-1]
        origDir.pop()
        origDir=["/"+"/".join(origDir)]
        temp=cd(origDir,True)
        temp=currentDict()[toAdd] = {}
        currentDir=originalDir
    else:
        temp = currentDict()[args[0]] = {}
    
    
    args=args[0].split("/")
    fs.sync()

def sudo(args):
    numTry=1
    pw=""
    try:
        pw=input("[sudo] password for "+username+": ")
        for i in range(1,3):
            if pw!=rootpass:
                numTry+=1
                pw=input("[sudo] password for "+username+": ")
            else:
                numTry=0
                break
            
    except KeyboardInterrupt:
        pass
    try:
        if pw==rootpass and len(args)>0:
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
    helpMsg="""The following are the basic commands and its functions:
    ls    | lists the files and directories present in the current directory
    cd    | change directory
    cat   | shows the content of file(s)
    sudo  | elevates privilege
    mkdir | creates a new directory
    """
    print(helpMsg)

# =============================================================================
# All Key Linux commands are defined.
# =============================================================================

def exitProgram(args):
    raise RuntimeError
    
def inputRun(raw):
    if type(raw)==str:
        fullCmd=raw.split()
    elif type(raw)==list:
        fullCmd=raw
    if len(fullCmd)>0:
        cmd=fullCmd[0]
    else:
        return
    if cmd in COMMANDS:
        try:
            COMMANDS[cmd](fullCmd[1:])
        except RuntimeError:
            raise RuntimeError
    else:
        print(cmd+": command not found")

def getName():
    name=input("Whats your name?")


    
# Initialization
init(fs)

# Define commands
COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir, "sudo":sudo, "exit":exitProgram,
            "cat":cat, "help":userHelp}




while True:
    try:
        if len(currentDir)>=2:
            if currentDir[0]=="home" and currentDir[1]==username:
                if len(currentDir)==2:
                    raw = input(username+"@"+"ThinkPadX1C:~ $ ")
                elif len(currentDir)>=2:
                    homeDir=dupList(currentDir)[2:]
                    raw = input(username+"@"+"ThinkPadX1C:~/"+"/".join(homeDir)+" $ ")
            else:
                raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(currentDir)+" $ ")
        else:
            raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(currentDir)+" $ ")
        inputRun(raw)
    except RuntimeError:
        break

save=input("Game stopped. Do you want to save the game? (y/n) >>> ")
if save.lower()=="y":
    fs.sync()
    fs.close()
    input('Game saved. Press the Enter key to shutdown...')
else:
    # Removes the files generated by shelves
    if os.path.exists("filesystem.fs.dir"):
        os.remove("filesystem.fs.dir")
    if os.path.exists("filesystem.fs.dat"):
        os.remove("filesystem.fs.dat")
    if os.path.exists("filesystem.fs.bak"):
        os.remove("filesystem.fs.bak")
    input('Game NOT saved. Press the Enter key to shutdown...')
