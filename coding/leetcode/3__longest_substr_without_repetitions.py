def length_of_longest_substring(s):
    """
    Get the longest substring with unique symbols

    :param s:
    :return:
    """

    if not s:
        return 0

    if len(s) == 1:
        return 1

    p = 0
    result = 0
    cur_dct = {}

    while len(s) - 1 >= p:

        if s[p] not in cur_dct.keys():
            cur_dct[s[p]] = p
            p += 1

            if len(cur_dct) > result:
                result = len(cur_dct)

        else:

            p = cur_dct[s[p]] + 1
            cur_dct = {}

    return result


if __name__ == '__main__':

    # s = "wpwfwkeww"
    # s = "abcabcbb"
    s = "pwwkew"

    print(length_of_longest_substring(s))
