def swap(number):
    digits = [ch for ch in str(number)]
    largest = number
    smallest = number
    for i in range(len(digits)):
        for j in range(len(digits)):
            digits[i], digits[j] = digits[j], digits[i]
            if digits[0] != '0':
                joined = int(''.join(digits))
                largest = max(joined, largest)
                smallest = min(joined, smallest)
            digits = [ch for ch in str(number)]
    return (largest, smallest)
