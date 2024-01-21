def distinct_digit_year(year):
    next_distinct = year + 1
    while len(set(str(next_distinct))) != len(str(next_distinct)):
        next_distinct += 1
    return next_distinct
