from preloaded import animals, elements


def chinese_zodiac(year):
    element_idx = ((year - 1924) // 2) % 5
    animal_idx = (year - 1924) % 12
    sign = f'{elements[element_idx]} {animals[animal_idx]}'
    return sign
