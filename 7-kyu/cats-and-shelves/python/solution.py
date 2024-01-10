def solution(start, finish):
    diff = finish - start
    if diff < 3:
        return diff
    return 1 + solution(start, finish - 3)
