import time

def make_me_slow():
    now = time.time()
    while True:
        if time.time() - now > 7:
            break