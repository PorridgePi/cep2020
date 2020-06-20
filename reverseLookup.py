def reverseLookup(dic, key):
    newDic = {}
    for i in dic:
        if dic[i] not in newDic:
            newDic[dic[i]] = [i]
        else:
            newDic[dic[i]].append(i)

    if key not in newDic:
        return []
    else:
        return newDic[key]        


dict1 = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 3, 'g': 4, 'h': 6,
        'i': 1, 'j': 3, 'k': 2, 'l': 10, 'm': 1
        }

print("This is the dictionary.")
print(dict1)

print("\nMultiple keys: keys with value 1")
print(reverseLookup(dict1, 1))

print("\nA single key: key with value 6")
print(reverseLookup(dict1, 6))

print("\nNo keys: no value with key 9")
print(reverseLookup(dict1, 9))
