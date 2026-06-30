def timestamp_to_seconds(timestamp):
    h, m, s = map(int, timestamp.split(':'))
    return h * 3600 + m * 60 + s

def evil_code_medal(*args):
    user_time, gold, silver, bronze = map(timestamp_to_seconds, args)
    if user_time < gold:
        return 'Gold'
    elif user_time < silver:
        return 'Silver'
    elif user_time < bronze:
        return 'Bronze'
    return 'None'
