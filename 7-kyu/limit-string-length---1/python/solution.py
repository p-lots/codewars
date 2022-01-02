def solution(st, limit):
    return f'{st[:limit]}...' if limit < len(st) else st
