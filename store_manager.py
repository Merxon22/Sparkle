import pygame, sys
import webbrowser

class StoreManager:
    def __init__(self):
        self.pi_ghost = pygame.image.load('Images/pi store ghost.png')
        self.pi_pumpkin = pygame.image.load('Images/pi store pumpkin.png')
        self.pi_castle = pygame.image.load('Images/pi store castle.png')
        self.pi_logo = pygame.image.load('Images/piLogo.png')
        self.pi_logo = pygame.transform.scale(self.pi_logo, (25, 25))
    
    def render_store(self, screen):
        screen.blit(self.pi_ghost, [80, 360])
        screen.blit(self.pi_pumpkin, [80, 420])
        screen.blit(self.pi_castle, [80, 480])
        screen.blit(self.pi_logo, [268, 373])
        screen.blit(self.pi_logo, [268, 433])
        screen.blit(self.pi_logo, [268, 493])

        if(self.is_clicked(self.pi_ghost, [80, 360]) or self.is_clicked(self.pi_pumpkin, [80, 420]) or self.is_clicked(self.pi_castle, [80, 480])):
            webbrowser.open('https://sandbox.minepi.com/app/alittleidlegame')

    def is_clicked(self, obj, obj_pos):
        cursor_pos = pygame.mouse.get_pos()
        obj_rect = obj.get_rect()
        x_is_in = cursor_pos[0] <= obj_rect.right + obj_pos[0] and cursor_pos[0] >= obj_pos[0]
        y_is_in = cursor_pos[1] <= obj_rect.bottom + obj_pos[1] and cursor_pos[1] >= obj_pos[1]
        is_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_clicked = True
        return x_is_in and y_is_in and is_clicked
