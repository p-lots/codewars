def elevator_distance(array):
    return sum(abs(x - y) for x, y in zip(array, array[1:]))
