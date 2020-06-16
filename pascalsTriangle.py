def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def pascals_triangle(r):
    for n in range(r):
        a = fact(n)
        b = fact(r)
        c = n-r
        print(c)
        d = fact(c)
        print(a,b,d)

pascals_triangle(4)