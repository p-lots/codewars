def has_unique_digits(year):
    year_lst = []
    while year > 0:
        year_lst.append(year % 10)
        year //= 10
    return len(set(year_lst)) == len(year_lst)

def distinct_digit_year(year):
    ret = year + 1
    while not has_unique_digits(ret):
        ret += 1
    return ret