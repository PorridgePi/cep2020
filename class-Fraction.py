import fractions

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


a = fractions.Fraction()

class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    def __str__(self):
        return str(self.num)+'/'+str(self.denom)
    def __add__(self, other):
        top = self.num * other.denom + other.num * self.denom
        bottom = self.denom * other.denom
        hcf = gcd(top, bottom)
        return Fraction(int(top/hcf), int(bottom/hcf))
    
    def __sub__(self, other):
        pass


a = Fraction(2,9)
b = Fraction(1,3)

print(a+b)







