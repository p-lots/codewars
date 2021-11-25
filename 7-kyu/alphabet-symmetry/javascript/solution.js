def solve(arr):
    ret = []
    for word in arr:
        ret.append(sum(1 for i, ch in enumerate(word.lower()) if i == ord(ch) - ord('a')))
    return ret