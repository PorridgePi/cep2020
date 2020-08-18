import random
import time


welcomeMsg="""Welcome, hacker.
You mission is to hack this computer running Linux.
Key in 'help' anytime to view the help guide.
"""


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
    o=input(name+"@"+"ThinkPadX1C:"+loc+" $ ")
    while o=="":
        o=input(name+"@"+"ThinkPadX1C:"+loc+" $ ")
    order=split(o)
    
    cmd=order[0]
    if cmd=="exit":
        raise SyntaxError
    elif cmd=="cd" and len(order)==2:
        return order[1]
    elif cmd=="cd" and len(order)>2:
        print("-bash: cd: too many arguments")
    elif cmd=="sudo":
        try:
            pw=input("[sudo] password for "+name+": ")
        except KeyboardInterrupt:
            pass
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