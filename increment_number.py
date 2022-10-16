import pygame

class IncrementNumber():
    def __init__(self, value, pos, init_time):
        self.value = value
        self.pos = pos
        self.init_time = init_time

        self.font = pygame.font.SysFont("arial", 10, True, False)
        self.txt = self.font.render('+' + str(value), True, (255,255,255))