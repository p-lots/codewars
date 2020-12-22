def calc_cat_age(cat_years):
    if cat_years < 15:
        return 0
    cat_years -= 15
    if cat_years < 9:
        return 1
    return 2 + (cat_years - 9) // 4

def calc_dog_age(dog_years):
    if dog_years < 15:
        return 0
    dog_years -= 15
    if dog_years < 9:
        return 1
    return 2 + (dog_years - 9) // 5

def owned_cat_and_dog(cat_years, dog_years):
    return [calc_cat_age(cat_years), calc_dog_age(dog_years)]
