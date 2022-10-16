import pygame, sys
pygame.init()

class MenuManager:
    def __init__(self):
        self.reward_button = pygame.image.load('./Images/reward.png')
        self.star_button = pygame.image.load('./Images/star.png')
        self.store_button = pygame.image.load('./Images/store.png')

        y = 605
        self.store_pos = (75, y)
        self.reward_pos = (275, y)
        self.star_pos = (175, y)
    
    def render_button(self, screen):
        screen.blit(self.store_button, self.store_pos)
        screen.blit(self.star_button, self.star_pos)
        screen.blit(self.reward_button, self.reward_pos)

