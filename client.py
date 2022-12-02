import pygame
from network import Network
from player import Player

WIDTH, HEIGHT = 1000, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

client_numbner = 0

    

def redraw_window(screen, player1, player2, bullets):
    screen.fill((255,255,255))
    player1.draw(screen)
    player2.draw(screen)
    for bullet in bullets: 
        bullet.draw(screen)
    pygame.display.update()
    
def main():
    bullets = []
    run = True
    n = Network()
    p1 = n.get_p()
    
    clock =pygame.time.Clock()
    
    while run:
        clock.tick(60)
        
        response = n.send((p1, bullets))
        if response != None:
            p2, bullets = response
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        bullet = p1.input()
        if bullet != None:
            bullets.append(bullet)
        
        for bullet in bullets:
            bullet.move_bullet()
        
        p1.reload_frames -= 1 
        if p1.reload_frames <= 0:
            p1.allow_shoot = True
        
        redraw_window(screen, p1, p2, bullets)
    
main()
