def next_day_of_week(current_day, available_week_days):
    avail_days = [ch for ch in f'{available_week_days:b}'.zfill(8)[::-1]]
    idx = current_day % len(avail_days)
    ret = avail_days[idx]
    while ret != '1':
        idx += 1
        idx = idx % len(avail_days)
        ret = avail_days[idx]
    return idx + 1
