def gps(s, x):
    speeds = [3600 * (max(b - a, 0)) / s for a, b in zip(x, x[1:])]
    return int(max(speeds)) if len(speeds) > 0 else 0