def crap(garden, bags, cap):
    at_count = 0
    for row in garden:
        at_count += row.count('@')
        if row.count('D') > 0:
            return 'Dog!!'
    return 'Clean' if at_count <= bags * cap else 'Cr@p'