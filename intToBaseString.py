def to_string(n, base):
    l = ['A','B','C','D','E','F']
    if n // base == 0:
        if n >= 10:
            return l[n-10]
        else:
            return str(n)
    else:
        result = ""

        rem = n % base
        if rem >= 10:
            result = l[rem-10] + result
        else:
            result += str(rem)
        
        return to_string(int(n//base), base) + result

print(to_string(6543,2))