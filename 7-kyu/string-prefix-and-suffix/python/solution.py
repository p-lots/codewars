def solve(st):
    if not st or len(st) == 1:
        return 0
    pres = [st[:i] for i in range(1, len(st) // 2 + 1)]
    sufs = [st[len(st) - i:] for i in range(1, len(st) // 2 + 1)]
    only_matches = [len(pre) for pre, suf in zip(pres, sufs) if pre == suf]
    return max(only_matches) if only_matches else 0