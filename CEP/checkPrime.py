def isPrime(n): 
    prime=[2,3]
    if n <= 1: 
        return False
    c = 0
    for i in prime:
        c+=1
        if i<=n/2:
            if n%i==0:
                return(False)
                break
            else:
#                print(c*2-1)
                prime.append(c*2+1)
        else:
            return(True)

def p(n):
    for i in range(2, int(n/2+1)): 
        print(i)
        if n % i == 0: 
            return False; 
    return True

n = int(input('Enter number: '))
print(True) if isPrime(n) else print(False)


#71597