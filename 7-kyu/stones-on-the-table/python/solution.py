def solution(stones):
    return sum(1 for lhs, rhs in zip(stones, stones[1:]) if lhs == rhs)