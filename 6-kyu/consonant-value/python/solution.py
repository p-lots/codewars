def solve(s):
    split_arr = []
    split_str = ''
    for ch in s:
        if ch in 'aeiou':
            split_arr.append(split_str)
            split_str = ''
        else:
            split_str += ch
    return max(map(lambda item: sum(ord(ch) - 96 for ch in item), split_arr))