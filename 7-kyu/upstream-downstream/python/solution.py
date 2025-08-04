def time(distance, boat_speed, stream):
    direction, stream_speed = stream.split(' ')
    stream_speed = int(stream_speed)
    boat_speed += -stream_speed if direction[0] == 'U' else stream_speed
    t = round(distance / boat_speed, 2)
    return t
