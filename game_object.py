import pygame

class Game_object:
    def __init__(self, x, y, width, height, color, velocity) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.velocity = velocity
        self.dir = 'right'
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)