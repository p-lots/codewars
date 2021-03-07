def sayMeOperations(stringNumbers):
    ret = []
    numbers = list(map(int, stringNumbers.split()))
    for lhs, rhs, result in zip(numbers, numbers[1:], numbers[2:]):
        if lhs + rhs == result:
            ret.append('addition')
        elif lhs - rhs == result:
            ret.append('subtraction')
        elif lhs * rhs == result:
            ret.append('multiplication')
        elif lhs // rhs == result:
            ret.append('division')
    return ', '.join(ret)