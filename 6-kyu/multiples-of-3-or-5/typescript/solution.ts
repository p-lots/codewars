from functools import reduce

def solution(number):
    if number <= 3:
        return 3 if number == 3 else 0
    return reduce(lambda acc, num: acc + num, list(filter(lambda item: item % 3 == 0 or item % 5 == 0, list(range(3, number)))))