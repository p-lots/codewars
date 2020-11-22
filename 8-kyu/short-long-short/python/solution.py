def solution(a, b):
    strings = [a, b]
    long = max(strings, key=len)
    short = min(strings, key=len)
    return f'{short}{long}{short}'
