def recurrence(values):
    smallest_idx = values.index(min(values))
    values = values[smallest_idx:]
    for first, second, third, fourth in zip(values, values[1:], values[2:], values[3:]):
        if first < second < third < fourth:
            return True
    return False
