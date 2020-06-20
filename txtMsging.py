def txt2num(txt):
    txt = txt.upper()

    keys = {
        1: ['.', ',', '?', '!', ':'],
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z'],
        0: [' ']
        }

    result = ''

    for i in txt:
        for num in keys:
            if i in keys[num]:
                result += str(num)*(keys[num].index(i)+1)
    return result


def main():
    txt = input("Please input your text message or press Enter to exit.\n>>> ")
    if txt == '':
        raise UnboundLocalError
    print(txt2num(txt))


while True:
    try:
        main()
    except UnboundLocalError:
        print('Goodbye!')
        break
