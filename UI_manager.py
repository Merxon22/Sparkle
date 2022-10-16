import sys, pygame
pygame.init()

class UiManager():
    def __init__(self):
        pass

    def render_ui(self, screen, level, num_sparkles, sparkle_rate):
        level_font = pygame.font.SysFont("arial", 20, True, False)
        level_txt = level_font.render('LEVEL ' + str(level-1), True, (255, 255, 255))
        screen.blit(level_txt, (170, 30))

        sparkle_font = pygame.font.SysFont("arial", 30, True, False)
        sparkle_txt = sparkle_font.render(str(num_sparkles) + ' SPARKLES', True, (255,255,255))
        screen.blit(sparkle_txt, (120, 80))

        rate_font = pygame.font.SysFont("arial", 20, True, False)
        rate_txt = rate_font.render('+' + str(sparkle_rate) + ' sparkles/s', True, (255,255,255))
        screen.blit(rate_txt, (140, 120))
