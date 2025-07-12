from preloaded import Hero

def move(self, direction):
    currY, currX = [int(num) for num in self.position]
    if direction == 'left':
        if currX == 0:
            raise IndexError
        currX -= 1
    elif direction == 'right':
        if currX == 4:
            raise IndexError
        currX += 1
    elif direction == 'up':
        if currY == 0:
            raise IndexError
        currY -= 1
    elif direction == 'down':
        if currY == 4:
            raise IndexError
        currY += 1
    self.position = f'{currY}{currX}'
    return self.position
    
Hero.move = move
