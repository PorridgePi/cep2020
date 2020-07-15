def occurrence(s1, s2):
    result = 0
    if s1 == s2:
        return 1
    elif len(s2) >= len(s1):
        return 0
    else:
        if s1[0:len(s2)] == s2:
            result += 1
            return result + occurrence(s1[len(s2):],s2)
        else:
            return result + occurrence(s1[1:],s2)