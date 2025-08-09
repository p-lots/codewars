def total_amount_visible(top_num, num_of_sides):
    total_dots = num_of_sides * (num_of_sides + 1) // 2
    opposite_top = num_of_sides + 1 - top_num
    return total_dots - opposite_top
