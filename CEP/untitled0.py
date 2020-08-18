def spinWords(s):
    words=[]
    word=""
    for i in s:
        if i!=" ":
            word+=i
        else:
            words.append(word)
            word=""
    words.append(word)
    for i in range(len(words)):
        if len(words[i])>=5:
            words[i]=words[i][::-1]
    result=""
    for i in words:
        result+=i
        if i!=words[-1]:
            result+=" "
    return result
            