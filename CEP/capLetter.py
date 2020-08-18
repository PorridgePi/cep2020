def cap(c,caps=True):
    up=ord(c)>=65 and ord(c)<97
    if up and caps:
        return c
    elif not up and caps:
        return chr(ord(c)-32)
    elif up and not caps:
        return chr(ord(c)+32)
    elif not up and not caps:
        return c
def split(phrase):
    l=[]
    word=""
    for i in phrase:
        if i!=" ":
            word+=cap(i,False)
        else:
            if word!=" " and word!="":
                l.append(word)
                word=""

    if word!=" " and word!="":
        l.append(word)
    return l

def title_case(title, minor_words=''):
    words=split(title)
    minor=split(minor_words)
    
    result=cap(words[0][0])+words[0][1:]+" "
    words.remove(words[0])
    
    for i in words:
        if i in minor:
            result=result+i
        else:
            result=result+cap(i[0])+i[1:]
        if i!=words[-1]:
            result+=" "
        
    return result

