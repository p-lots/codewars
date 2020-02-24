from math import ceil

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        new_red = self.avg_color(self.color[0], other.color[0], self.volume, other.volume)
        new_green = self.avg_color(self.color[1], other.color[1], self.volume, other.volume)
        new_blue = self.avg_color(self.color[2], other.color[2], self.volume, other.volume)
        return Potion((new_red, new_green, new_blue), self.volume + other.volume)
    
    def avg_color(self, color1, color2, volume1, volume2):
        weight1 = volume1 / (volume1 + volume2) * 2
        weight2 = volume2 / (volume1 + volume2) * 2
        return ceil((color1 * weight1 + color2 * weight2) / 2)