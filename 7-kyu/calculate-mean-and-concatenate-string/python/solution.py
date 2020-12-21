def mean(lst):
    numbers = [int(ch) for ch in lst if ch.isdigit()]
    letters = [ch for ch in lst if ch.isalpha()]
    return [sum(numbers) / len(numbers), ''.join(letters)]
    