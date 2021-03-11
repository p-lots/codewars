def find_smallest(numbers,to_return):
    return [min(numbers), numbers.index(min(numbers))][to_return == 'index']
