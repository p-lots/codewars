def fizz_buzz_cuckoo_clock(time):
    time_split = time.split(':')
    hours = int(time_split[0])
    minutes = int(time_split[1])
    if minutes == 0:
        count = 12 if hours % 12 == 0 else hours - 12 if hours > 12 else hours
        return ' '.join(['Cuckoo' for _ in range(count)])
    elif minutes == 30:
        return 'Cuckoo'
    elif minutes % 15 == 0:
        return 'Fizz Buzz'
    elif minutes % 5 == 0:
        return 'Buzz'
    elif minutes % 3 == 0:
        return 'Fizz'
    return 'tick'