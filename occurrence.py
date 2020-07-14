def occurrence(s1, s2):
    result = 0
    if s1 == s2:
        return 1
    elif len(str(s2)) >= len(str(s1)):
        return 0
    else:
        if str(s1)[0:len(str(s2))] == s2:
            result += 1
        
            