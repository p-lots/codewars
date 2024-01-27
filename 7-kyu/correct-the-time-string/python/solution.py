import re

def time_correct(t):
    if not t:
        return None if t is None else ""
    elif re.fullmatch(r"[0-9]{2}:[0-9]{2}:[0-9]{2}", t) is None:
        return None
    hours, minutes, seconds = [int(n) for n in t.split(':')]
    if hours > 23 or minutes > 59 or seconds > 59:
        minutes += seconds // 60
        seconds %= 60
        hours += minutes // 60
        minutes %= 60
        hours %= 24
    return f'{hours:02}:{minutes:02}:{seconds:02}'
