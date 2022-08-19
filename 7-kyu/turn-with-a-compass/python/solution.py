def change_dir(dirs, facing, turn):
    curr_dir = dirs.index(facing)
    curr_dir += turn // 45
    return dirs[curr_dir % len(dirs)]

def direction(facing, turn):
    cw_dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    ccw_dirs = ['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE']
    return change_dir(cw_dirs, facing, turn) if turn > 0 else change_dir(ccw_dirs, facing, abs(turn))
