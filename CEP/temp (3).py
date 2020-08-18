from math import sqrt
def magnitude(x1,y1,x2,y2):
    return(sqrt((x2-x1)**2+(y2-y1)**2))

def area3(x1,y1,x2,y2,x3,y3):
    a=magnitude(x1,y1,x2,y2)
    b=magnitude(x2,y2,x3,y3)
    c=magnitude(x1,y1,x3,y3)
    s=(a+b+c)
    
    return (round(sqrt(s*(s-a)*(s-b)*(s-c))/1,14))
    #return sqrt(((a+(b+c))*(c-(a-b))*(c+(a-b))*(a+(b-c))))/4

print(area3(1,2,6,9,10,-1))
