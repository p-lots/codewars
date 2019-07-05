def sumDigits(number):
    sum = 0
    for x in str(abs(number)):
        sum += int(x)
    return sum
    