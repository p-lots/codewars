def find_missing_number(numbers):
    expected_sum = (len(numbers) + 1) * (len(numbers) + 2) // 2
    return expected_sum - sum(numbers)