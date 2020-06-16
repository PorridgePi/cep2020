def reverseNum(origNum):
    lastLetters = origNum[4:8]
    lastDigits = ''
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

    for c in lastLetters:
        c = c.lower()
        for i in range(0, 9):
            if c in digits[str(i)]:
                lastDigits += str(i)
                break
    return origNum[0:4]+lastDigits


if __name__ == "__main__":
    print(reverseNum('8123BOOK'))
