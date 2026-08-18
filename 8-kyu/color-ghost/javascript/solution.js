import random

class Ghost(object):
    def __init__(self):
        self.all_colors = ['white', 'yellow', 'purple', 'red']
        color_idx = random.randrange(len(self.all_colors))
        self.color = self.all_colors[color_idx]