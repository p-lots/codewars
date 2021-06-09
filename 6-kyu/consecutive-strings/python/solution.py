def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    longest = ''
    for i in range(len(strarr)):
        curr = ''
        if i + k < len(strarr):
            curr = ''.join(strarr[i:i + k])
        else:
            curr = ''.join(strarr[i:])
        if len(curr) > len(longest):
            longest = curr
    return longest
