import pygame, sys
from pygame.locals import *
pygame.init()
FPS=20
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((300, 600), 0, 20)
pygame.display.set_caption("PI-game")
running=True
move_x=10
move_y=10
diagram=pygame.image.load("earth.jpg")
diagram_rect=diagram.get_rect()
#image_position_x=
#image_position_y=
score=0
speed=[5,5]
while running:
    screen.fill((250, 100, 250))
    
    height=diagram.get_rect().height
    width=diagram.get_rect().width
    scale= score+1
    diagram=pygame.transform.scale(diagram, (width*0.05*scale, height*0.05*scale))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            x, y=event.pos
            if diagram.get_rect().collidepoint(x,y):
                score+=1
    #speed movement of earth
    #diagram_rect = diagram_rect.move(speed)
    #if diagram_rect.left < 0 or diagram_rect.right > 600:
     #   speed[0] = -speed[0]
    #if diagram_rect.top < 0 or diagram_rect.bottom > 300:
     #   speed[1] = -speed[1]
    screen.blit(diagram, (300, 250))
    #screen.blit(diagram, diagram_rect)
    font=pygame.font.SysFont("arial", 50, True, False)
    surface=font.render(str(score), True, (255, 000, 000))
    screen.blit(surface, (140, 100))

    pygame.display.flip()