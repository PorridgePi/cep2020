class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num)+'/'+str(self.denom)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def reduce(self):
        hcf = self.gcd(self.num, self.denom)
        if hcf == self.denom:
            return int(self.num/hcf)
        else:
            return Fraction(int(self.num/hcf), int(self.denom/hcf))

    def inverse(self):
        return Fraction(self.denom, self.num).reduce()

    def __add__(self, other):
        top = self.num * other.denom + other.num * self.denom
        bottom = self.denom * other.denom
        return Fraction(top, bottom).reduce()

    def __sub__(self, other):
        top = self.num * other.denom - other.num * self.denom
        bottom = self.denom * other.denom
        return Fraction(top, bottom).reduce()

    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom).reduce()

    def __truediv__(self, other):
        return self * Fraction(other.denom, other.num)

    def __float__(self):
        return self.num/self.denom
