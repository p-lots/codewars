def solution(n, b):
    return [number for number in range(2 ** n) if number & b]
