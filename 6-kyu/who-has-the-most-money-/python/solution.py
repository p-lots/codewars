def most_money(students):
    if len(students) == 1:
        return students[0].name
    amts_names = list(map(lambda student: (student.fives * 5 + student.tens * 10 + student.twenties * 20, student.name), students))
    amts_names_max = max(amts_names, key=lambda item: item[0])
    amts_names_min = min(amts_names, key=lambda item: item[0])
    return amts_names_max[1] if amts_names_max != amts_names_min else "all"