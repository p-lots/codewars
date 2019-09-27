def solve(s):
    ret = 0
    vowel_str = ''
    for ch in s:
        if ch in 'aeiou':
            vowel_str += ch
        else:
            ret = max(len(vowel_str), ret)
            vowel_str = ''
    return ret