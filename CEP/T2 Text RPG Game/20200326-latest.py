import shelve

fs = shelve.open('filesystem.fs', writeback=True)
current_dir = []

def init(fs):
    # create users, passwords and initialize filesystem
    global username, rootpass
    rootpass="poop"
    username = input('What do you want your username to be? ')

    fs[""] = {"bin":{},"boot":{},"dev":{},"etc":{},"home":{username: {}},"lib":{},"opt":{},"sbin":{},"srv":{},"tmp":{},"usr":{},"proc":{}}

def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    d = fs[""]
    for key in current_dir:
        d = d[key]
    return d

def ls(args):
    print ('Contents of directory', "/" + "/".join(current_dir) + ':')
    for i in current_dictionary():
        print( i)

def cd(args):
    if len(args) != 1:
        print ("Usage: cd <directory>")
        return

    if args[0] == "..":
        if len(current_dir) == 0:
            print ("Cannot go above root")
        else:
            current_dir.pop()
    elif args[0] not in current_dictionary():
        print ("Directory " + args[0] + " not found")
    else:
        current_dir.append(args[0])


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

COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir, "sudo":sudo, "exit":exitProgram}

init(fs)

while True:
    try:
        if len(current_dir)>=2:
            if current_dir[0]=="home" and current_dir[1]==username:
                raw = input(username+"@"+"ThinkPadX1C:~ $ ")
            else:
                raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(current_dir)+" $ ")
        else:
            raw = input(username+"@"+"ThinkPadX1C:"+"/"+"/".join(current_dir)+" $ ")
        inputRun(raw)
    except RuntimeError:
        break

input('Press the Enter key to shutdown...')