def array_leaders(numbers):
    totals = [sum(numbers[i:]) - numbers[i] for i in range(len(numbers))]
    return [numbers[i] for i, total in enumerate(totals) if numbers[i] > total]