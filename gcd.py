def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)

# If b is 0 then
#     Return a
# Else
#     Set c equal to the remainder when a is divided by b
#     Return the greatest common divisor of b and c

