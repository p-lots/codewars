import datetime

def create_datetime(for_date):
    date_split = for_date.replace(',', '').split()
    date_split[1] = date_split[1].zfill(2)
    return datetime.datetime.strptime(' '.join(date_split), '%B %d %Y')

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    return entered_code and correct_code and entered_code == correct_code and create_datetime(current_date) <= create_datetime(expiration_date)