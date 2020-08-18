class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


class LineSegment(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def slope(self):
        return (self.point2.y - self.point1.y)/(self.point2.x - self.point1.x)

    def length(self):
        return ((self.point2.y - self.point1.y)**2+(self.point2.x - self.point1.x)**2)**0.5
