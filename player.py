from game_object import *
from bullet import Bullet

class Player(Game_object):
    def __init__(self, x, y, width, height, color, velocity) -> None:
        super().__init__(x, y, width, height, color, velocity)
        self.allow_shoot = True
        self.reload_frames = 0
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            self.dir = ""
            if keys[pygame.K_UP]:
                self.y -=  self.velocity
                self.dir += 'n'
            elif keys[pygame.K_DOWN]:
                self.y +=  self.velocity
                self.dir += 's'
                
            if keys[pygame.K_LEFT]:
                self.x -=  self.velocity
                self.dir += 'w'
            elif keys[pygame.K_RIGHT]:
                self.x +=  self.velocity
                self.dir += 'e'

        if keys[pygame.K_SPACE] and self.allow_shoot:
            self.allow_shoot = False
            self. reload_frames = 20
            return Bullet(self.x + self.width/2, self.y + self.height/2, 3, 3, (0,0,0), 10, self.dir)
        
        self.rect = (self.x, self.y, self.width, self.height)
        
