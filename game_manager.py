import this
from unicodedata import name
import pygame, sys
from UI_manager import UiManager

from menu_manager import MenuManager
from star_manager import StarManager
from store_manager import StoreManager
pygame.init()
from Background import BackgroundManager
pygame.joystick.init()

class GameManager():
    def __init__(self):
        self.background_manager = BackgroundManager()
        self.menu_manager = MenuManager()
        self.star_manager = StarManager()
        self.ui_manager = UiManager()
        self.store_manager = StoreManager()

        self.width, self.height = 400, 700
        self.size = (400, 700)
        self.screen = pygame.display.set_mode(self.size)

        self.current_level = 1
        self.num_sparkles = 0
        self.sparkle_rate = 0
        self.history_level = 2
        self.sparkle_multiplier = 1
        self.last_sparkle_update_time = 0

        #item
        self.item_stack = [0,0,0]
        self.item_price = [15,50,200]     
    

    def add_sparkle(self, num):
        self.num_sparkles += num

    def run_game(self):
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print(len(joysticks))

        while True:
            self.check_sparkle_update()

            if self.current_level != 0 and self.current_level != 1 and self.current_level != 5:
                self.current_level = self.history_level

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.current_level == 1:
                    self.current_level = 2


            self.background_manager.render_background(self.screen, self.current_level)
            if self.current_level == 0:
                self.menu_manager.render_button(self.screen, self)
            elif self.current_level == 5:
                self.menu_manager.render_button(self.screen, self)
                self.store_manager.render_store(self.screen, self)
            elif self.current_level > 1:
                self.menu_manager.render_button(self.screen, self)
                self.star_manager.render_star(self.screen, self.current_level, self, self.sparkle_multiplier)
                self.ui_manager.render_ui(self.screen, self.current_level, self.num_sparkles, self.sparkle_rate)
            pygame.display.flip()

    def check_sparkle_update(self):
        if pygame.time.get_ticks() - self.last_sparkle_update_time >= 100:
            self.num_sparkles += self.sparkle_rate / 10
            self.last_sparkle_update_time = int(pygame.time.get_ticks() / 100) * 100

if __name__ == '__main__':
    game = GameManager()
    game.run_game()