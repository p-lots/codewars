def high_and_low(numbers):
    arr = []
    for n in numbers.split():
        arr.append(int(n))
    return str(max(arr)) + ' ' + str(min(arr))