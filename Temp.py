import pygame
from pygame.locals import *
pygame.init()
size = width, height= 400, 700
speed = [3, 3]
screen=pygame.display.set_mode((400, 700))
pygame.display.set_caption("SPARKLEs")
running=True
earth=pygame.image.load("Earth.jpg")
earth_rect=earth.get_rect()

score=0
while running:
    screen.fill((250, 250, 000))
    screen.blit(earth, (150, 250))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            #print(pos)
            if earth.get_rect().collidepoint(pos):
                score+=1
    #earth_rect2=earth_rect.move(speed)
    #if earth_rect2.left < 0 or earth_rect2.right > 400:
     #   speed[0] = -speed[0]
    #if earth_rect2.top < 0 or earth_rect2.bottom > 700:
        #speed[1] = -speed[1]
    #screen.blit(earth, earth_rect, earth_rect2)
    #screen.blit(earth, earth_rect)
   
    font=pygame.font.SysFont("arial", 50, True, False)
    surface=font.render(str(score), True, (255, 0, 0))
    screen.blit(surface, (200, 100))
    pygame.display.flip()