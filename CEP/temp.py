def bin2den(n):
    l=len(str(n))
    result=0
    for i in range(l):

        two=2**i
        digit=int(str(n)[-1-i])

        result+=digit*two
    return result
