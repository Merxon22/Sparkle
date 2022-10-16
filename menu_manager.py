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
    
    def render_button(self, screen, game_manager):
        '''
        executed every frame
        '''
        click=pygame.mouse.get_pressed()
        if click[0]==True:
            pos=pygame.mouse.get_pos()
            if self.reward_button.get_rect().collidepoint(pos):
                game_manager.current_level=0
            elif self.star_button.get_rect().collidepoint(pos):
                game_manager.current_level=1
            elif self.store_button.get_rect().collidepoint(pos):
                game_manager.current_level=2
        screen.blit(self.store_button, self.store_pos)
        screen.blit(self.star_button, self.star_pos)
        screen.blit(self.reward_button, self.reward_pos)

    
    


                    

