def what_is_the_time(time_in_mirror):
    hours, mins = list(map(int, time_in_mirror.split(':')))
    hours_in_mirror = 12 - hours if mins == 0 else (12 - hours - 1 + 12) % 12
    mins_in_mirror = 60 - mins if mins > 0 else 0
    if hours_in_mirror == 0:
        hours_in_mirror = 12
    return f'{hours_in_mirror:02}:{mins_in_mirror:02}'
