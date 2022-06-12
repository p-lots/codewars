def factory(x):
    def multiplier(arr):
        return [n * x for n in arr]
    return multiplier
