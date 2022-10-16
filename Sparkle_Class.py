import pygame
from pygame.locals import *

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
        font1=pygame.font.SysFont("Times New Romans", 50, True, False)
        surface1=font1.render((str(str(name)+'/t'+str(stage)+ ": "+str(level))+ str("Coin posessed: ")+str(coins_possessed)), True, (255, 255, 0))
        return surface1
   
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
    def __init__(self):
        #display_game(self)
        Sparkles.__init__(self, name, coins_possessed, click_values, level, stage, star_color, level_threshold)
    def display_game(self):
        print(1)
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
        surface1=Sparkles.current_worth(self, name, coins_possessed, level, stage)
        screen.blit(surface1, (140, 100))
        pygame.display.flip()



Sparkle=Sparkles("User1", 34500, 2, 3, "beginner", "yellow", 40000 )
Sparkle.display_game()



        #foundation()
        #beginner()
        #amateur()
        #expert()
        #half_step_master()
        #master()
        #grand_master()
        #great_grand_master()
        #legendary_grand_master()
        #sage()