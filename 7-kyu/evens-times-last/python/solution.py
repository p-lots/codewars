def even_last(numbers): 
    return sum(numbers[-1] * numbers[i] for i in range(0, len(numbers), 2))
