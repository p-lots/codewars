def set_the_alarms_up(time, n):
    ALARM_INTERVAL = 5
    starting_hours, starting_minutes = [int(elem) for elem in time.split(':')]
    alarms = []
    for interval in range(n):
        elapsed_minutes = starting_minutes + ALARM_INTERVAL * interval
        next_minutes = elapsed_minutes % 60
        next_hours = (starting_hours + elapsed_minutes // 60) % 24
        next_timestamp = f'{next_hours:02}:{next_minutes:02}'
        alarms.append(next_timestamp)
    return alarms