def generator(a):
    b = 1
    while True:
        yield f'{a} x {b} = {a * b}'
        b += 1