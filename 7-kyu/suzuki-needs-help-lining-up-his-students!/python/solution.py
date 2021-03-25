def lineup_students(strng):
    return sorted(strng.split(), key=lambda elem: (len(elem), elem), reverse=True)
