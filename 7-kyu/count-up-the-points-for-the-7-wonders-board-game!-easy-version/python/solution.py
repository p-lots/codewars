def seven_wonders_science(compasses, gears, tablets):
    cards = [compasses, gears, tablets]
    complete_sets = min(cards) * 7
    square_sum = sum(n ** 2 for n in cards)
    total_points = complete_sets + square_sum
    return total_points
