import pygame, sys
import webbrowser

class StoreManager:
    def __init__(self):
        self.store_1 = pygame.image.load('Images/store 1.png')
        self.store_2 = pygame.image.load('Images/store 2.png')
        self.store_3 = pygame.image.load('Images/store 3.png')

        self.pi_ghost = pygame.image.load('Images/pi store ghost.png')
        self.pi_pumpkin = pygame.image.load('Images/pi store pumpkin.png')
        self.pi_castle = pygame.image.load('Images/pi store castle.png')
        self.pi_logo = pygame.image.load('Images/piLogo.png')
        self.pi_logo = pygame.transform.scale(self.pi_logo, (25, 25))

        self.cach_sound = pygame.mixer.Sound("Sound\Cash.mp3")

    
    def render_store(self, screen, game_manager):
        screen.blit(self.store_1, [80, 95])
        screen.blit(self.store_2, [80, 140])
        screen.blit(self.store_3, [80, 185])

        price_font = pygame.font.SysFont("arial", 16, True, False)
        price1_txt = price_font.render(str(game_manager.item_price[0]), True, (255, 255, 255))
        price2_txt = price_font.render(str(game_manager.item_price[1]), True, (255, 255, 255))
        price3_txt = price_font.render(str(game_manager.item_price[2]), True, (255, 255, 255))
        screen.blit(price1_txt, (240, 105))
        screen.blit(price2_txt, (240, 150))
        screen.blit(price3_txt, (240, 195))


        screen.blit(self.pi_ghost, [80, 360])
        screen.blit(self.pi_pumpkin, [80, 420])
        screen.blit(self.pi_castle, [80, 480])
        screen.blit(self.pi_logo, [268, 373])
        screen.blit(self.pi_logo, [268, 433])
        screen.blit(self.pi_logo, [268, 493])

        events = pygame.event.get()

        if(self.is_clicked(self.pi_ghost, [80, 360], events) or self.is_clicked(self.pi_pumpkin, [80, 420], events) or self.is_clicked(self.pi_castle, [80, 480], events)):
            print('linked clicked')
            webbrowser.open('https://sandbox.minepi.com/app/alittleidlegame')



        # items
        if self.is_clicked(self.store_1, [80, 95], events) and game_manager.num_sparkles >= game_manager.item_price[0]:
            print(1)
            game_manager.num_sparkles -= game_manager.item_price[0]
            game_manager.item_price[0] = int(game_manager.item_price[0] ** 1.2)
            game_manager.sparkle_rate += 3
            game_manager.item_stack[0] = game_manager.item_stack[0] + 1
            pygame.mixer.Sound.play(self.cach_sound)

        if self.is_clicked(self.store_2, [80, 140], events) and game_manager.num_sparkles >= game_manager.item_price[1]:
            print(2)
            game_manager.num_sparkles -= game_manager.item_price[1]
            game_manager.item_price[1] = int(game_manager.item_price[1] ** 1.2)
            game_manager.sparkle_multiplier *= 1.75
            game_manager.item_stack[1] = game_manager.item_stack[1] + 1
            pygame.mixer.Sound.play(self.cach_sound)
            
        if self.is_clicked(self.store_1, [80, 185], events) and game_manager.num_sparkles >= game_manager.item_price[2]:
            print(3)
            game_manager.num_sparkles -= game_manager.item_price[2]
            game_manager.item_price[2] = int(game_manager.item_price[2] ** 1.2)
            game_manager.history_level += 1
            game_manager.item_stack[2] = game_manager.item_stack[2] + 1
            pygame.mixer.Sound.play(self.cach_sound)


    def is_clicked(self, obj, obj_pos, events):
        cursor_pos = pygame.mouse.get_pos()
        obj_rect = obj.get_rect()
        x_is_in = cursor_pos[0] <= obj_rect.right + obj_pos[0] and cursor_pos[0] >= obj_pos[0]
        y_is_in = cursor_pos[1] <= obj_rect.bottom + obj_pos[1] and cursor_pos[1] >= obj_pos[1]
        is_clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_clicked = True
        return x_is_in and y_is_in and is_clicked
