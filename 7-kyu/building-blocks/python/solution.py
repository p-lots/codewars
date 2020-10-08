class Block:
    def __init__(self, arr):
        self.width = arr[0]
        self.length = arr[1]
        self.height = arr[2]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        return self.width * self.length * self.height
    def get_surface_area(self):
        return 2 * (self.length * self.height + self.height * self.width + self.length * self.width)