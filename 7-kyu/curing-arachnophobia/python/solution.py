def draw_spider(leg_size, body_size, mouth, eye):
    LEGS_LOOKUP = {1: "^ ^", 2: '/\\ /\\', 3: '/╲ ╱\\', 4: '╱╲ ╱╲'}
    legs = LEGS_LOOKUP[leg_size].split()
    body = [f'{"(" * body_size}', f'{")" * body_size}']
    eyes = eye * (1 << (body_size - 1))
    spider = f'{legs[0]}{body[0]}{eyes}{mouth}{eyes}{body[1]}{legs[1]}'
    return spider
