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
earth_pos = (150, 250)
earth_check_distance = 65

score=0

def check_cursor_distance_from_star(cursor_pos, earth_pos):
    earth_center = (earth_pos[0] + earth_rect.height/2, earth_pos[1] + earth_rect.width/2)
    return ((cursor_pos[0]-earth_center[0])**2 + (cursor_pos[1]-earth_center[1])**2)**0.5

while running:
    screen.fill((250, 250, 000))
    screen.blit(earth, earth_pos)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            #print(pos)
            if check_cursor_distance_from_star(pos, earth_pos) <= earth_check_distance:
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

