def get_section_id(scroll, sizes):
    start = -1
    total = -1
    for dist in sizes:
        if total >= scroll:
            return start
        start += 1
        total += dist
    return start if total >= scroll else -1
