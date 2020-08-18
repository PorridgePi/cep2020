def shift(a,n):
    i=ord(a)+n%26
    if ord(a)>=97:
        if i>122:
            return chr(i-26)
        elif i>=97:
            return chr(i)
        elif i<97 and i>90:
            return chr(i+26)
    else:
        if i>90:
            return chr(i-26)
        elif i>=65:
            return chr(i)
        elif i<65:
            return chr(i+26)

def caesar_encrypt(msg,n):
    result=""
    for i in msg:
        result+=shift(i,n)
    return result

def caesar_decrypt(msg):
    for n in range(26):
        n+=1
        result=""
        for i in msg:
            result+=shift(i,-n)
        print (result)
        
        