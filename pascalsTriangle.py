def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def pascals_triangle(i):
    if type(i)!=int or i<=0:
        return "Input must be positive and an integer!"
    result = []
    for n in range(i):
        for r in range(n+1):
            result.append(int(fact(n)/(fact(r)*fact(n-r))))
    
    return result

for i in range(10):
    print(pascals_triangle(i))