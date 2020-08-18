import random
import time


welcomeMsg="""Welcome, hacker.
You mission is to hack this computer running Linux.
Key in 'help' anytime to view the help guide.
"""

rootpass="Ab13!@23kdaweef"

# Although Python has a inbuilt string.split() function, there may be extra
# spaces. For example "a a  a" will result in ['a', 'a', '', 'a']

def split(phrase):
    l=[]
    word=""
    for i in phrase:
        if i!=" ":
            word+=i.lower()
        else:
            if word!=" " and word!="":
                l.append(word)
                word=""

    if word!=" " and word!="":
        l.append(word)
    return l

def helpMsg():
    print("""You can use left right up down""")


def getInput(name,loc):
    if loc=="/home/"+name:
        o=input(name+"@"+"ThinkPadX1C:~ $ ")
    else:
        o=input(name+"@"+"ThinkPadX1C:"+loc+" $ ")
    while o=="":
        o=input(name+"@"+"ThinkPadX1C:"+loc+" $ ")
    order=split(o)
    
    cmd=order[0]
    if cmd=="exit":
        raise SyntaxError
    elif cmd=="cd":
        if len(order)==1:
            return "/home/"+name
        elif len(order)==2:
            return order[1]
        elif len(order)>2:
            print("-bash: cd: too many arguments")
    elif cmd=="sudo":
        numTry=1
        try:
            pw=input("[sudo] password for "+name+": ")
            for i in range(1,3):
                if pw!=rootpass:
                    numTry+=1
                    pw=input("[sudo] password for "+name+": ")
                else:
                    break
            if pw!=rootpass:
                print("sudo: "+str(numTry)+" incorrect password attempt")
        except KeyboardInterrupt:
            if numTry>0:
                print("\nsudo: "+str(numTry)+" incorrect password attempt")
            
    else:
        print(order[0]+": command not found")
        
scenes=['lake','house','forest']


def main():
    print(welcomeMsg)
    name=input("What's your name?\n>>> ")
    global root
    root={"home":name,
               "bin":"",
               "etc":""}
    loc="/home/"+root["home"]
    while True:
        try:
            newloc=getInput(name,loc)
            if newloc!=None:
                loc=newloc
        except SyntaxError:
            break

    currentScene=random.choice(scenes)
    print(currentScene)

main()