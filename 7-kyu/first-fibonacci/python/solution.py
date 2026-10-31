def solution(first, second):
    while second - first >= 0:
        first, second = second - first, first
    return second, first + second
