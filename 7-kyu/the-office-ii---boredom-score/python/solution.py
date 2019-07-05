def boredom(staff):
    lookup_table = {
        'accounts': 1, 'finance': 2, 'canteen': 10,
        'regulation': 3, 'trading': 6, 'change': 6,
        'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25
    }
    ret = 0
    for key, value in staff.items():
        ret += lookup_table[value]
    return 'party time!!' if ret >= 100 else 'i can handle this' if ret > 80 else 'kill me now'