import datetime

def to_day_of_year(date):
    day, month, year = date
    curr_date = datetime.date(year, month, day)
    first_day = datetime.date(year, 1, 1)
    return int((curr_date - first_day).total_seconds() / (60 * 60 * 24)) + 1
