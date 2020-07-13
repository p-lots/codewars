def solution(digits):
    greatest = int(digits[:5])
    for i in range(len(digits) - 4):
        if int(digits[i:i + 5]) > greatest:
            greatest = int(digits[i:i + 5])
    return greatest