from base64 import urlsafe_b64encode, urlsafe_b64decode
import random
import string

def encrypt(k,s):
    encryptedChars = []
    for i in range(len(s)):
        key_c=k[i%len(k)]
        encryptedChar=chr(ord(s[i])+ord(key_c)%256)
        encryptedChars.append(encryptedChar)
    encryptedStr="".join(encryptedChars)
    return urlsafe_b64encode(encryptedStr.encode())

def decrypt(k,s):
    s=urlsafe_b64decode(s).decode()
    decryptedChars = []
    for i in range(len(s)):
        key_c=k[i%len(k)]
        decryptedChar=chr(ord(s[i])-ord(key_c)%256)
        decryptedChars.append(decryptedChar)
    decryptedStr="".join(decryptedChars)
    return decryptedStr

def genPass(fro=8,to=16):
    letters=string.ascii_letters
    passList=[]
    for i in range(random.randint(fro,to)):
        passList.append(random.choice(letters))
    password="".join(passList)
    return password

