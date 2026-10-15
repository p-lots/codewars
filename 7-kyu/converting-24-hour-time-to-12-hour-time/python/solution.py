def to_12_hour_time(time_string):
    # The timestring will always be four digits using
    # "hhmm" format.
    # return 'h:mm am' or 'h:mm pm'
    hours = int(time_string[:2])
    minutes = time_string[2:]
    meridian = 'am' if hours < 12 else 'pm'
    converted = f'{hours % 12 if hours not in [0, 12] else 12}:{minutes} {meridian}'
    return converted