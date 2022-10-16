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
        screen.blit(self.store_button, self.store_pos)
        screen.blit(self.star_button, self.star_pos)
        screen.blit(self.reward_button, self.reward_pos)

        if self.is_clicked(self.reward_button, self.reward_pos):
            game_manager.current_level=0
        elif self.is_clicked(self.store_button, self.store_pos):
            game_manager.current_level=5
        elif self.is_clicked(self.star_button, self.star_pos):
            game_manager.current_level=2

    def is_clicked(self, obj, obj_pos):
        cursor_pos = pygame.mouse.get_pos()
        obj_rect = obj.get_rect()
        x_is_in = cursor_pos[0] <= obj_rect.right + obj_pos[0] and cursor_pos[0] >= obj_pos[0]
        y_is_in = cursor_pos[1] <= obj_rect.bottom + obj_pos[1] and cursor_pos[1] >= obj_pos[1]
        is_clicked = False
        return x_is_in and y_is_in and pygame.mouse.get_pressed()[0]
    


                    

