def sort_reindeer(reindeer_names):
    return [item[1] for item in sorted(enumerate(reindeer_names), key=lambda elem: (elem[1].split()[1], elem[0]))]