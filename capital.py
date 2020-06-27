def capital(l):
    result = []
    for i in l:
        if 'state' in i:
            result.append('The capital of ' + i['state'] + ' is ' + i['capital'])
        else:
            result.append('The capital of ' + i['country'] + ' is ' + i['capital'])

    return result


print(capital([{'state': 'Maine', 'capital': 'Augusta'}]))
