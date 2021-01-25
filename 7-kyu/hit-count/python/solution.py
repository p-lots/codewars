def counter_effect(hit_count):
    return [list(range(n + 1)) for n in map(int, hit_count)]
