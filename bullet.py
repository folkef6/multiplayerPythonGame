from game_object import *

class Bullet(Game_object):
    
    def __init__(self, x, y, width, height, color, velocity, dir) -> None:
        super().__init__(x, y, width, height, color, velocity)
        self.dir = dir
    
    def move_bullet(self):
        if self.dir == "n":
            self.y -= self.velocity
        if self.dir == "s":
            self.y += self.velocity
        if self.dir == "w":
            self.x -= self.velocity
        if self.dir == "r":
            self.x += self.velocity
        if self.dir == "nw":
            self.x -= self.velocity
            self.y -= self.velocity
        if self.dir == "sw":
            self.x -= self.velocity
            self.y += self.velocity
        if self.dir == "ne":
            self.x += self.velocity
            self.y -= self.velocity
        if self.dir == "se":
            self.x += self.velocity
            self.y += self.velocity
            
        
    
        self.rect = (self.x, self.y, self.width, self.height)