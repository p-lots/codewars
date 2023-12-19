from datetime import datetime

def day_of_week(from_date):
    dte = datetime.strptime(from_date, '%d/%m/%Y')
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][dte.weekday()]
