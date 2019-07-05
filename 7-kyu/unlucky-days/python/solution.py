from datetime import date, timedelta

def unlucky_days(year):
    d = date(year, 1, 1)
    while d.weekday() != 4:
        d += timedelta(days=1)
    ret = 0
    while d.year == year:
        d += timedelta(weeks=1)
        if d.day == 13:
            ret += 1
    return ret