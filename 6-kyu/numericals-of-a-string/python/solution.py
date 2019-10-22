def numericals(s):
    ret = ''
    counts = {}
    for i in range(len(s)):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
        ret += str(counts[s[i]])
    return ret