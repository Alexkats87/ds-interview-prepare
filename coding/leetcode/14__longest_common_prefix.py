def longest_common_prefix(strs):
    """
    Get the longest common prefix among all the strings from list
    """

    from copy import deepcopy

    if not strs:
        return ""

    result = deepcopy(strs[0])

    for s in strs[1:]:
        length = min(len(result), len(s))
        result = result[:length]
        for i in range(length):
            if result[i] != s[i]:
                result = result[:i]
                break

    print(result)


if __name__ == '__main__':
    # ss = ["flower", "flow", "floight"]
    # ss = ["dog", "racecar", "car"]
    ss = ["a", "b"]

    longest_common_prefix(ss)



