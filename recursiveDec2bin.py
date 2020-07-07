def d2b(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return d2b(n//2) + str(n%2)

if __name__ == "__main__":
    for i in range(10):
        print(d2b(i))
    