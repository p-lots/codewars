def converter(mpg):
    GAL_IN_L = 1.609344
    MILES_IN_KM = 4.54609188
    return round(mpg * GAL_IN_L / MILES_IN_KM, 2)