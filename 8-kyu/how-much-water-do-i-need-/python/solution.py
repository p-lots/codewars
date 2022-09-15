def how_much_water(water, load, clothes):
    if load * 2 < clothes:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    calculated_water = water * 1.1 ** abs(load - clothes)
    return round(calculated_water, 2)
