from functools import reduce

def _at(lhs, rhs):
    return (lhs + rhs) + (lhs - rhs) + (lhs * rhs) + (lhs // rhs) if rhs != 0 else None

def evaluate(equation):
    equ = [int(term) for term in equation.split(' @ ')]
    try:
        return reduce(_at, equ)
    except:
        return None
