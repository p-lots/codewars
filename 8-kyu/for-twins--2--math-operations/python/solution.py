def ice_brick_volume(radius, bottle_length, rim_length):
    height = bottle_length - rim_length
    return height * radius * radius * 2
