def grader(score):
    score = round(score * 100)
    if not (60 <= score <= 100):
        return 'F'
    if score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    return 'A'
