def part(arr):
    related_terms = ['Partridge', 'PearTree', 'Chat', 'Dan',
        'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    count = 0
    for term in arr:
        if term in related_terms:
            count += 1
    return f"Mine's a Pint{'!' * count}" if count else "Lynn, I've pierced my foot on a spike!!"