def letter_count(s):
    result = {}
    for i in s:
        i = i.lower()
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


print(letter_count('arithmetics'))
