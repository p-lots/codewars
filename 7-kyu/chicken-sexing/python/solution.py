def score(lhs, rhs):
    if lhs == rhs:
        return 1
    elif rhs == '?' or lhs == '?':
        return 0.5
    return 0

def correctness(bobs_decisions, expert_decisions): 
    return sum(score(lhs, rhs) for lhs, rhs in zip(bobs_decisions, expert_decisions))
