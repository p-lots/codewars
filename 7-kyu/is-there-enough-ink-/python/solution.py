def enough_ink(image, r, g, b):
    rgb_needed = [0, 0, 0]
    for row in image:
        for pixel in row:
            red = int(pixel[:2], 16)
            green = int(pixel[2:4], 16)
            blue = int(pixel[4:], 16)
            rgb_needed = [rgb_needed[0] + 255 - red, rgb_needed[1] + 255 - green, rgb_needed[2] + 255 - blue]
    rgb_have = [r, g, b]
    return all(needed <= have for needed, have in zip(rgb_needed, rgb_have))
