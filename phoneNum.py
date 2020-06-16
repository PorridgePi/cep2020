print('This program will generate all possible spellings of the\nlast four digits of any number')

while True:
    origNum = input('Enter phone number (xxxxxxxx): ')

    digits = {
            '0': ('0'),
            '1': ('1'),
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
            }

    for a in digits[origNum[4]]:
        for b in digits[origNum[5]]:
            for c in digits[origNum[6]]:
                for d in digits[origNum[7]]:
                    print(origNum[0:4]+a+b+c+d)

    conti=input('Enter another phone number? (y/n): ')
    if conti == 'n':
        break
    