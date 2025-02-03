def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    hour_24 = hour + (12 if period == 'pm' and hour < 12 else -12 if hour == 12 and period == 'am' else 0)
    return f'{hour_24:02}{minute:02}'
