def quadrant(x,y):
    left=None
    up=None
    if x>0:
        left=False
    elif x<0:
        left=True
    if y>0:
        up= True
    elif y<0:
        up = False
    
    if up and left:
        return 2
    elif up and not left:
        return 1
    elif not up and left:
        return 3
    elif not up and not left:
        return 4
    
def last_point(x1,y1,x2,y2,x3,y3):
    if x1==x2:
        x4=x3
    elif x2==x3:
        x4=x1
    elif x1==x3:
        x4=x2

    if y1==y2:
        y4=y3
    elif y2==y3:
        y4=y1
    elif y1==y3:
        y4=y2
    return(x4,y4)
    
def short_v(phrase):
    result=""
    l=phrase.split("-")
    for i in l:
        result+=i[0]
    return result


def biggest(n,h,v):
    # n, the length of the sides of the square cake
    # h, the distance of the horizontal cut from the top edge of the cake
    # v, the distance of the vertical cut from the left edge of the cake
    if h>=n/2 and v>=n/2:
        return h*v*4
    elif h>=n/2 and v<n/2:
        return h*(n-v)*4
    elif h<n/2 and v>=n/2:
        return (n-h)*v*4
    elif h<n/2 and v<n/2:
        return (n-h)*(n-v)*4
    
def count_distinct_digits(n):
    l=[]
    for i in str(n):
        if i not in l:
            l.append(i)
    return len(l)

def num_factors(n):
    if n==1:
        return 1
    i=1
    l=[]
    while i<n:
        if n%i==0:
            l.append(i)    
        i+=1
    return len(l)

def minmax(l,d,x):
    for i in range(l,d+1,1):
        s=0
        for a in str(i):
            s+=int(a)
        if s==x:
            n=i
            break
    for i in range(d,l-1,-1):
        s=0
        for a in str(i):
            s+=int(a)
        if s==x:
            m=i
            break
    return[n,m]
    
def double_check(leg1,leg2,leg3,total):
    result=[]
    l1=[]
    l1d={}
    i=1
    t=0
    l2d={}
    for i in range(total//leg1+1):
        l1.append(leg1*i)
    for i in l1:
        l2=[]
        left=total-i
        for a in range(left//leg2+1):
            l2.append(leg2*a)
        l1d[i]=l2
    for i in l1d:
        l2d={}
        for a in l1d[i]:
            left=total-i-a
            if left%leg3==0:
                l2d[a]=left/leg3
            
        l1d[i]=l2d
    toPop=[]
    for i in l1d:
        if l1d[i]=={}:
            toPop.append(i)
    for i in toPop:
        l1d.pop(i)
            
    for i in l1d:
        for a in l1d[i]:
            result.append(str(int(i/leg1))+" "+str(int(a/leg2))+" "+str(int(l1d[i][a])))

    return result