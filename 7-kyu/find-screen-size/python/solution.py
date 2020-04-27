def find_screen_height(width, ratio):
    ratio_split = ratio.split(':')
    width_ratio = int(ratio_split[0])
    height_ratio = int(ratio_split[1])
    return f'{width}x{width * height_ratio // width_ratio}'