def get_grade(s1, s2, s3):
    grades = [s1, s2, s3]
    avg = sum(grades) / len(grades)
    if 90 <= avg <= 100: return 'A'
    elif 80 <= avg < 90: return 'B'
    elif 70 <= avg < 80: return 'C'
    elif 60 <= avg < 70: return 'D'
    return 'F'
    