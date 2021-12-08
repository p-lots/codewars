def fly_by(lamps, drone):
    drone_len = len(drone)
    lamps_len = len(lamps)
    return f'{"o" * ((drone_len - 1) if drone_len > lamps_len else drone_len)}{"x" * min(lamps_len - drone_len, lamps_len)}'