class Lamp(object):
    def __init__(self, c):
        self.color = c
        self.on = False
    
    def state(self):
        return 'The lamp is {}.'.format('on' if self.on else 'off')
    
    def toggle_switch(self):
        self.on = not self.on