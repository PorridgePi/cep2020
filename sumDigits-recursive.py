def sumDigits(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        return int(sumDigits(n[1:])) + int(n[0])