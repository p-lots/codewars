def human_years_cat_years_dog_years(human_years):
    pet_years = lambda human_yrs, factor: 15 * (human_yrs > 0) + \
                                           9 * (human_yrs > 1) + \
                                           (human_yrs - 2) * factor * (human_yrs > 2)
    CAT_FACTOR = 4
    DOG_FACTOR = 5
    cat_years = pet_years(human_years, CAT_FACTOR)
    dog_years = pet_years(human_years, DOG_FACTOR)
    return [human_years, cat_years, dog_years]
