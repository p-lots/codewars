def time_convert(num):
    if num < 1:
        return '00:00'
    hrs, mins = str(num // 60).zfill(2), str(num % 60).zfill(2)
    return f'{hrs}:{mins}'
