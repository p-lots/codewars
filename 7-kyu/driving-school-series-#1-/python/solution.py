def passed(lst):
    passed = [n for n in lst if n < 19]
    return round(sum(passed) / len(passed)) if len(passed) > 0 else 'No pass scores registered.'
    