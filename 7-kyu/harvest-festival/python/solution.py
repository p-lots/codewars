def plant(seed, water, fert, temp):
    return f'{("-" * water + seed * fert) * water}' if 20 <= temp <= 30 else f'{"-" * (water * water)}{seed}'
