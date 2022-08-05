def sort_by_binary_ones(numList):
    s = sorted(numList)
    s = sorted(s, key=lambda elem: len(f'{elem:b}'))
    return sorted(s, key=lambda elem: f'{elem:b}'.count('1'), reverse=True)
