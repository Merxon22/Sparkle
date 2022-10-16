import pygame, sys
from pygame.locals import *

from Background import BackgroundManager, background

class Sparkles:
    pygame.init()
    def __init__(self, name, coins_possessed, click_values, level, stage, star_color, level_threshold):
        self.name=name
        self.coins_possessed=coins_possessed
        self.click_values=click_values
        self.level=level
        self.stage=stage
        self.star_color=star_color
        self.level_threshold=level_threshold
    def current_worth(self, name, coins_possessed, level, stage):
        font1=pygame.font.SysFont("Times New Romans", 15, True, False)
        surface1=font1.render(str(name), True, (255, 0, 0))
        surface2=font1.render(str("Coins possessed: "+str(coins_possessed)),True, (255, 255, 0))
        surface3=font1.render(str(str(stage)+" : "+str("Level ")+str(level)), True, (255, 0, 255))
        return [surface1, surface2, surface3]
   
    """ def display_game(self):
        pygame.init()
        FPS=20
        fpsClock=pygame.time.Clock()
        screen=pygame.display.set_mode((400, 700))
        pygame.display.set_caption("SPARKLEs")
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
        self.current_worth(self, name, coins_possessed, level, stage)
        pygame.display.flip() """
class Display(Sparkles):
    
    def __init__(self, name, coins_possessed, click_values, level, stage, star_color, level_threshold):
        #display_game(self)
        Sparkles.__init__(self, name, coins_possessed, click_values, level, stage, star_color, level_threshold)
        
    
    def display_game(self):
        pygame.init()
                
        FPS=60
        fpsClock=pygame.time.Clock()
        screen=pygame.display.set_mode((400, 700))
        pygame.display.set_caption("SPARKLEs")
        running=True
        surface1=Sparkles.current_worth(self, self.name, self.coins_possessed, self.level, self.stage)
        screen.blit(surface1[0], (10, 100))
        screen.blit(surface1[1], (10, 120))
        screen.blit(surface1[2], (10, 140))
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.quit

            pygame.display.flip()
    def foundation(self, coins_possessed, click_values=1, level=1, star_color=(255, 255, 0), initializing_value=100):
        display_game()
        earth=pygame.image.load("stage1.png")
        earth_rect=earth.get_rect()
        earth_pos = (150, 250)
        earth_check_distance = 65
        score=coins_possessed
        def check_cursor_distance_from_star(cursor_pos, earth_pos):
            earth_center = (earth_pos[0] + earth_rect.height/2, earth_pos[1] + earth_rect.width/2)
            return ((cursor_pos[0]-earth_center[0])**2 + (cursor_pos[1]-earth_center[1])**2)**0.5
        while running:
            
            screen.blit(earth, earth_pos)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()
                        #print(pos)
                    if check_cursor_distance_from_star(pos, earth_pos) <= earth_check_distance:
                        score+=1
            font=pygame.font.SysFont("arial", 50, True, False)
            surface=font.render(str(score), True, (255, 0, 0))
            screen.blit(surface, (200, 100))
            pygame.display.flip()
    def beginner(self, coins_possessed, click_values=2, level=1, star_color=(255, 0, 255), initializing_value=500):
        earth=pygame.image.load("Stage2.png")
        earth_rect=earth.get_rect()
        earth_pos = (150, 250)
        earth_check_distance = 65
        scores=coins_possessed
        def check_cursor_distance_from_star(cursor_pos, earth_pos):
            earth_center = (earth_pos[0] + earth_rect.height/2, earth_pos[1] + earth_rect.width/2)
            return ((cursor_pos[0]-earth_center[0])**2 + (cursor_pos[1]-earth_center[1])**2)**0.5
        while running:
            background(level)
            screen.blit(earth, earth_pos)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()
                        #print(pos)
                    if check_cursor_distance_from_star(pos, earth_pos) <= earth_check_distance:
                        score+=2
            font=pygame.font.SysFont("arial", 50, True, False)
            surface=font.render(str(score), True, (255, 0, 0))
            screen.blit(surface, (200, 100))
            pygame.display.flip()
    def amateur(self, coins_possessed, click_values=3, level=1, star_color=(0, 255, 255), initializing_value=3000):
        earth=pygame.image.load("Earth.jpg")
        earth_rect=earth.get_rect()
        earth_pos = (150, 250)
        earth_check_distance = 65
        scores=coins_possessed
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
                        score+=3
            font=pygame.font.SysFont("arial", 50, True, False)
            surface=font.render(str(score), True, (255, 0, 0))
            screen.blit(surface, (200, 100))
            pygame.display.flip()
    def expert(self, coins_possessed, click_values=4, level=1, star_color=(0, 0, 255), initializing_value=15000):
        earth=pygame.image.load("Earth.jpg")
        earth_rect=earth.get_rect()
        earth_pos = (150, 250)
        earth_check_distance = 65
        scores=coins_possessed
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
                        score+=4
            font=pygame.font.SysFont("arial", 50, True, False)
            surface=font.render(str(score), True, (255, 0, 0))
            screen.blit(surface, (200, 100))
            pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False



Sparkle=Display("User1", 34500, 2, 3, "Beginner", "yellow", 40000 )
Sparkle.display_game()


#extra code for stages

    