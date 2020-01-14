def longest(s):
    temp = s[0]
    ret = []
    for i in range(1, len(s)):
        if ord(temp[-1]) <= ord(s[i]):
            temp += s[i]
        else:
            ret.append(temp)
            temp = s[i]
    ret.append(temp)
    return max(ret, key=len) if ret else s