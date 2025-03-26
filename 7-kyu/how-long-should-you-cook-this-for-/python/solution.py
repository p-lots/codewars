from math import ceil, floor

def cooking_time(needed_power, minutes, seconds, power):
    pwr = int(power[:-1])
    needed_pwr = int(needed_power[:-1])
    ratio = needed_pwr / pwr
    total_secs = ceil((minutes * 60 + seconds) * ratio)
    return f'{floor(total_secs / 60)} minutes {total_secs % 60} seconds'
