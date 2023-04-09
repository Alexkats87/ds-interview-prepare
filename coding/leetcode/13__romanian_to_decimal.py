def roman_to_int(s):
    """
    Convert romanian number to integer number
    """

    if not s:
        return 0

    r = 0

    s = s.lower()

    while len(s) > 0 and s[0] == 'm':
        r += 1000
        s = s[1:]

    while len(s) > 1 and s[:2] == 'cm':
        r += 900
        s = s[2:]

    while len(s) > 0 and s[0] == 'd':
        r += 500
        s = s[1:]

    while len(s) > 1 and s[:2] == 'cd':
        r += 400
        s = s[2:]

    while len(s) > 0 and s[0] == 'c':
        r += 100
        s = s[1:]

    while len(s) > 1 and s[:2] == 'xc':
        r += 90
        s = s[2:]

    while len(s) > 0 and s[0] == 'l':
        r += 50
        s = s[1:]

    while len(s) > 1 and s[:2] == 'xl':
        r += 40
        s = s[2:]

    while len(s) > 0 and s[0] == 'x':
        r += 10
        s = s[1:]

    while len(s) > 1 and s[:2] == 'ix':
        r += 9
        s = s[2:]

    while len(s) > 0 and s[0] == 'v':
        r += 5
        s = s[1:]

    while len(s) > 1 and s[:2] == 'iv':
        r += 4
        s = s[2:]

    while len(s) > 0 and s[0] == 'i':
        r += 1
        s = s[1:]

    return r


if __name__ == '__main__':

    print(roman_to_int("MCDLXXVI"))
