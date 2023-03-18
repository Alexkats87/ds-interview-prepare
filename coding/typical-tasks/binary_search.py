"""
Find the first index where elements are different
"""

if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]

    r = len(a) - 1
    l = 0
    m = int((r - l) / 2)

    print(l, m, r)

    while r - l > 1:

        if a[m] == b[m]:
            l = m
            m = l + int((r - l) / 2.0)
            print(l, m, r, "eq")

        else:

            r = m
            m = int((r - l) / 2.0)
            print(l, m, r, "neq")

    # l will be equal to the last equal elements
    # r will be equal to the first not equal elements
