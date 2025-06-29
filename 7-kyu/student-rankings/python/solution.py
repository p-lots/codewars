def post_grades(students):
    students_split = [student.split(' - ') for student in students]
    rankings = []
    for id, _, grades in students_split:
        grades_split = [float(grade) for grade in grades.split(' ')]
        average = sum(grades_split) / len(grades_split)
        rankings.append((id, average))
    return sorted(rankings, key=lambda pair: pair[1], reverse=True)
