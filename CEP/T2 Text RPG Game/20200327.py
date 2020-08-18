import shelve
import os


fs = shelve.open('filesystem.fs', writeback=True)
current_dir = []
fs[""]={"a":{}}
def tooArgs(arg):
    print("-bash: "+arg+": too many arguments")

def genAccount():
    global username
    username = input('What do you want your username to be? ')
    
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
            "usr":{},
            "proc":{}
            }


def init(fs):
    # create users, passwords and initialize filesystem
    global username, rootpass
    rootpass="poop"
    username=""
    try:
        if type(fs[""])==dict:
            saved=input("Did you save your previous game? (y/n) >>> ")
            if saved.lower()=="y":
                uname=input("Input your username >>> ")
                if uname in fs[""]["home"]:
                    print("hi")
                    username=uname
        if username=="":
            genAccount()
    except:
        genAccount()
def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    d = fs[""]
    for key in current_dir:
        d = d[key]
    return d

def ls(args):
    print ('Contents of directory', "/" + "/".join(current_dir) + ':')
    for i in current_dictionary():
        print(i)

def cd(args):
    if len(args)<1:
        return
    elif len(args)>=2:
        tooArgs("cd")
# =============================================================================
#     if len(args) != 1:
#         print ("Usage: cd <directory>")
#         return
# =============================================================================

    elif args[0] == "..":
        if len(current_dir) == 0:
            print ("Cannot go above root")
        else:
            current_dir.pop()
    elif args[0] not in current_dictionary():
        print ("Directory " + args[0] + " not found")
    elif type(current_dictionary()[args[0]])==dict:
        current_dir.append(args[0])
    elif type(current_dictionary()[args[0]])!=dict:
        print("-bash: cd: "+args[0]+": Not a directory")

def cat(args):
    if len(args)<1:
        return
    else:
        for i in args:    
            if i not in current_dictionary():
                print ("cat: "+i+": No such file or directory")
            elif i == ".." or type(current_dictionary()[i])==dict:
                print("cat: "+i+": Is a directory")
            elif type(current_dictionary()[i])!=dict:
                print(current_dictionary()[i])

def mkdir(args):
    if len(args) != 1:
        print ("Usage: mkdir <directory>")
        return
    # create an empty directory there and sync back to shelve dictionary!
    d = current_dictionary()[args[0]] = {}
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


init(fs)

COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir, "sudo":sudo, "exit":exitProgram, "cat":cat}

while True:
    try:
##        print(current_dictionary())
        if len(current_dir)>=2:
            if current_dir[0]=="home" and current_dir[1]==username:
                if len(current_dir)==2:
                    raw = input(username+"@"+"ThinkPadX1C:~ $ ")
                elif len(current_dir)>=2:
                    homeDir=current_dir
                    homeDir.pop(0)
                    homeDir.pop(1)
                    raw = input(username+"@"+"ThinkPadX1C:~/"+"/".join(homeDir)+" $ ")
            else:
                raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(current_dir)+" $ ")
        else:
            raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(current_dir)+" $ ")
        inputRun(raw)
    except RuntimeError:
        break


save=input("Gave stopped. Do you want to save the game? (y/n) >>> ")
if save.lower()=="y":
    fs.sync()
    fs.close()
    input('Game saved. Press the Enter key to shutdown...')
else:
    if os.path.exists("filesystem.fs.dir"):
        os.remove("filesystem.fs.dir")
    if os.path.exists("filesystem.fs.dat"):
        os.remove("filesystem.fs.dat")
    if os.path.exists("filesystem.fs.bak"):
        os.remove("filesystem.fs.bak")
    else:
        pass
    input('Press the Enter key to shutdown...')
