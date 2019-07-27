def cube_checker(volume, side):
    if volume < 1 or side < 1:
        return False
    return volume == side ** 3