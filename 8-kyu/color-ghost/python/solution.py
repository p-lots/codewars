import random

class Ghost(object):
    all_colors = ['white', 'yellow', 'purple', 'red']
    def __init__(self):
        self.color = random.choice(Ghost.all_colors)