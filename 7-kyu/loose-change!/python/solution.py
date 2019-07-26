def change_count(change):
    total = sum(CHANGE[item] for item in change.split())
    return '${0:.2f}'.format(total)