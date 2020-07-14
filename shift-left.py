def shift_left(num,n):
    result = ''
    if n >= len(str(num)):
        n %= len(str(num))
    if n == 0:
        return num
    else:
        result = int(str(num)[1:]+str(num)[0])
        return shift_left(result, n-1)
