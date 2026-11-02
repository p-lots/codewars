from functools import cmp_to_key

def sort_func(a, b):
    if a.is_almost_empty and not b.is_almost_empty:
        return -1
    elif (not a.is_almost_empty) and b.is_almost_empty:
        return 1
    if a.expiry_days == b.expiry_days:
        return 1 if a.name[0].lower() > b.name[0].lower() else 0 if a.name[0].lower() == b.name[0].lower() else -1
    return 1 if a.expiry_days > b.expiry_days else -1 if a.expiry_days < b.expiry_days else 0

def fridge_organizer(items):
    nonspoiled = [item for item in items if item.expiry_days >= 0]
    return [item.name for item in sorted(nonspoiled, key=cmp_to_key(sort_func))]
