from collections import Counter

def repeat_sum(l):
    l_sets = [set(sublist) for sublist in l]
    all_numbers = set([n for lst in l for n in lst])
    all_count = Counter()
    for n in all_numbers:
        for sublist in l_sets:
            all_count[n] += int(n in sublist)
    return sum(n for n, count in all_count.items() if count > 1)
