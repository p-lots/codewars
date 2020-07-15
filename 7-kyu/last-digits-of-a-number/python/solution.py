def solution(n, d):
    if d <= 0:
        return []
    elif d >= len(str(n)):
        return list(map(int, str(n)))
    n = list(str(n)[::-1])
    return list(map(int, n[:d]))[::-1]