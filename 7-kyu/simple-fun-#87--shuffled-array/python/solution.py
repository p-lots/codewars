def shuffled_array(s):
    s.sort()
    for i in range(len(s)):
        curr_total = sum(s[:i] + s[i + 1:])
        s_copy = [n for n in s]
        if curr_total in s_copy:
            idx = s_copy.index(curr_total)
            del s_copy[idx]
            if curr_total == sum(s_copy):
                return s_copy