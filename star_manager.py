import pygame, sys

from increment_number import IncrementNumber
pygame.init()

class StarManager():
    def __init__(self):
        self.star1 = pygame.image.load('Images\stage1.png')
        self.star2 = pygame.image.load('Images\stage2.png')

        self.number_list = []
        self.click_sound = pygame.mixer.Sound("Sound\Squee.mp3")


    def check_cursor_distance_from_star(self, cursor_pos, star_pos, star_rect):
        earth_center = (star_pos[0] + star_rect.height/2, star_pos[1] + star_rect.width/2)
        return ((cursor_pos[0]-earth_center[0])**2 + (cursor_pos[1]-earth_center[1])**2)**0.5

    def render_star(self, screen, level, game_manager):
        star_image = None
        if level == 2:
            star_image = self.star1
        elif level == 3:
            star_image = self.star2
        original_scale = (star_image.get_width(), star_image.get_height())

        pos=pygame.mouse.get_pos()
        x_pos = 200 - star_image.get_width() / 2
        y_pos = 350 - star_image.get_height() / 2
        if self.check_cursor_distance_from_star(pos, (x_pos, y_pos), star_image.get_rect()) <= star_image.get_width() / 2:
            star_image = pygame.transform.scale(star_image, original_scale * 1.05)
        else:
            pass

        screen.blit(star_image, (x_pos, y_pos))

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if self.check_cursor_distance_from_star(pos, (x_pos, y_pos), star_image.get_rect()) <= star_image.get_width() / 2:
                    game_manager.add_sparkle(1)
                    pygame.mixer.Sound.play(self.click_sound)
                    # self.number_list.append(IncrementNumber(1, pos, pygame.time.get_ticks()))
        
        # self.update_all_numbers(screen)
    
    def update_all_numbers(self, screen):
        for number in self.number_list:
            if number.init_time + 1000 < pygame.time.get_ticks():
                screen.blit(number.txt, number.pos)