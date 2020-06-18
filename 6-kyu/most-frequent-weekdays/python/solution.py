from datetime import date, timedelta

def most_frequent_days(year):
    curr_date = date(year, 1, 1)
    one_day = timedelta(days=1)
    weekday_counts = [0, 0, 0, 0, 0, 0, 0]
    while curr_date <= date(year, 12, 31):
        weekday_counts[curr_date.weekday()] += 1
        curr_date += one_day
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return [day for count, day in zip(weekday_counts, days_of_week) if count == max(weekday_counts)]