import datetime

def age_in_days(year, month, day):
    age = datetime.date.today() - datetime.date(year, month, day)
    return f'You are {age.days} days old'