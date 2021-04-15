def year_days(year):
    def is_leap_year(y):
        return y % 4 == 0 and not y % 100 == 0 or y % 400 == 0
    return f'{year} has {366 if is_leap_year(year) else 365} days'
