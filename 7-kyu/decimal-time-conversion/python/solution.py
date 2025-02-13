def to_industrial(time):
    if isinstance(time, str):
        hours, minutes = [int(unit) for unit in time.split(':')]
        standard_seconds = minutes * 60 + hours * 60 * 60
    else:
        standard_seconds = time * 60
    decimal_hours = standard_seconds / 36 / 100
    return round(decimal_hours, 2)


def to_normal(time):
    decimal_hours, decimal_minutes = divmod(time, 1.0)
    standard_hours = int(decimal_hours)
    standard_minutes = round(decimal_minutes * 60)
    return f'{standard_hours}:{standard_minutes:02}'
