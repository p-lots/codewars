from functools import cmp_to_key

def sort_people(lhs, rhs):
    if lhs['age'] < rhs['age']:
        return -1
    elif lhs['age'] > rhs['age']:
        return 1
    return 1 if lhs['name'] < rhs['name'] else -1 if lhs['name'] > rhs['name'] else 0

def highest_age(group1,group2):
    all_groups = group1 + group2
    merged_people = []
    for person in all_groups:
        if not any(p['name'] == person['name'] for p in merged_people):
            merged_people.append(person)
            continue
        for merged_person in merged_people:
            if merged_person['name'] == person['name']:
                merged_person['age'] += person['age']
    oldest_group = max(merged_people, key=cmp_to_key(sort_people))
    return oldest_group['name']