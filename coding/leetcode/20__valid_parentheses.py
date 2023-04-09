def is_valid(s):
    """
    Check if parentheses are balanced
    """

    opens = ['(', '{', '[']
    closes = [')', '}', ']']
    d = dict(zip(opens, closes))

    if len(s) < 2:
        return False

    if s[0] in closes:
        return False

    stack = [s[0]]

    for e in s[1:]:

        if e in opens:
            stack.append(e)
        if e in closes:
            if not stack:
                return False

            poped = stack.pop()
            if d[poped] != e:
                return False

    if stack:
        return False
    return True
