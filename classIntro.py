class Coordinate(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z 
    def i(self):
        return "HALOGEN"

class zombie(object):
    def __init__(self):
        self.hp = 10
    
    def __str__(self):
        return "HP:"+str(self.hp)

    def loseHp(self, x):
        self.hp -= x
    
a = Coordinate(1,2,3)
print(a.x)
z = zombie()
print(z.hp)
z.loseHp(2)
print(z.hp)
print(z)