from datetime import datetime

def is_today(d):
    today = datetime.today()
    return d.year == today.year and d.month == today.month and d.day == today.day
