def even_last(numbers): 
    return sum(numbers[-1] * num for num in numbers[::2])
