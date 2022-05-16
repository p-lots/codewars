def determine_time(arr):
    total_seconds = 24 * 60 * 60
    for duration in arr:
        dur_split = duration.split(':')
        dur_hrs = int(dur_split[0])
        dur_mins = int(dur_split[1])
        dur_secs = int(dur_split[2])
        total_seconds -= (dur_hrs * 60 * 60) + (dur_mins * 60) - (dur_secs)
    return total_seconds >= 0
