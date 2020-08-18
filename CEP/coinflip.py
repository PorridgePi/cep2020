from random import choice
def toss():
    return choice(["H","T"])

sum=0

for i in range(500000000):
    prev=toss()
    print(prev+" ",end="")
    
    time=1
    total=1
    
    while time<3:
        current=toss()
        print(current+" ",end="")
        
        if current!=prev:
            time=1
            prev=current
        else:
            time+=1
        total+=1
    print("("+str(total)+" flips)")
    sum+=total
    
avg=sum/500000000
print("On average,",avg,"flips were needed. ")