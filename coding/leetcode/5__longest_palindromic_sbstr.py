def longest_palindrome(s):
    """
    Given a string s, get the longest palindromic substring in s.
    """

    result_1 = ''
    result_2 = ''

    if not s:
        return result_1

    if len(s) == 1:
        return s

    result_2 = s[0]

    # 1. Odd substrings checking
    p = 0

    while len(s) > p:
        i = 1

        while p-i >= 0 and p+i < len(s):
            if s[p-i] != s[p+i]:
                break

            cur_result_1 = s[p-i:p+i+1]
            if len(cur_result_1) > len(result_1):
                result_1 = cur_result_1

            i += 1

        p += 1

    # 2. Even substrings checking
    p1 = 0
    p2 = 1

    while len(s) > p2:
        i = 0

        while p1 - i >= 0 and p2 + i < len(s):
            if s[p1-i] != s[p2+i]:
                break

            cur_result_2 = s[p1-i:p2+i+1]
            if len(cur_result_2) > len(result_2):
                result_2 = cur_result_2

            i += 1

        p1 += 1
        p2 += 1

    if len(result_1) > len(result_2):
        return result_1
    return result_2


if __name__ == '__main__':

    s = 'ffabcdedcbasdgkdfjglabcba'
    print(longest_palindrome(s))







