def cube_times(times):
    times = sorted(times)
    avg = sum(times[1:-1]) / 3.0
    return (round(avg, 2), times[0])