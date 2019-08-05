def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    year_or_years = 'year' if abs(diff) == 1 else 'years'
    if diff > 0:
        return 'You are {0} {1} old.'.format(diff, year_or_years)
    elif diff == 0:
        return 'You were born this very year!'
    else:
        return 'You will be born in {0} {1}.'.format(abs(diff), year_or_years)