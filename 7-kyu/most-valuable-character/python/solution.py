def solve(strng):
    positions = [(len(strng) - strng[::-1].index(ch) - strng.index(ch), ch) for ch in set(strng)]
    return max(positions, key=lambda item: (item[0], ord('z') - ord(item[1])))[1]