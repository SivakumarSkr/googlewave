import pygame
from pygame.locals import *

pygame.init()
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
YELLOW = [255, 255, 0]


class Rectangle:
    def __init__(self, rect, direction, color):
        self.rect = rect
        self.direction = direction
        self.color = color

class Wave:
    def __init__(self):
        pygame.display.set_caption('Google Wave.')
        self.clock = pygame.time.Clock()
        self.height = 600
        self.width = 600
        self.screen_res = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)
        self.screen.fill(WHITE)
        self.end = False
        self.rect_width = 20
        self.rect_height = 20
        self.rect_gap = 30
        self.wave_start = 100
        self.init_wave_height = 200
        self.no_rect = 6
        self.wave_height_limit = 20
        self.speed = 1.2
        self.rect_list = []
        self.color_list = [BLUE, RED, YELLOW, BLUE, GREEN, RED]
        self.max_height = self.init_wave_height + self.wave_height_limit
        self.min_height = self.init_wave_height - self.wave_height_limit
        self.height_diff = 4
        self.init_square()
        while not self.end:
            self.loop()

    def init_square(self):
        squares = []
        for i in range(6):
            left_cord = self.wave_start + (i * self.rect_gap)
            rect = Rect(left_cord, self.init_wave_height + (i * self.height_diff), self.rect_width, self.rect_height)
            rectangle_obj = Rectangle(rect, 1, self.color_list[i])
            self.rect_list.append(rectangle_obj)
            
    def loop(self):
        self.event_loop()
        self.screen.fill(WHITE)
        self.draw_wave()
        pygame.display.update()
        self.clock.tick(60)
    
    @staticmethod
    def event_loop():
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

    def draw_wave(self):
        for wave in self.rect_list:
            self.change_direction(wave)
            self.change_speed(wave)
            pygame.draw.rect(self.screen, wave.color, wave.rect)
    
    def change_direction(self, wave):
        if wave.rect.y >= self.max_height:
            wave.direction = 0
        elif wave.rect.y <= self.min_height:
            wave.direction = 1

    def change_speed(self, wave):
        if wave.direction == 1:
            wave.rect.y += self.speed
        else:
            wave.rect.y -= self.speed
    
while True:
    game_obj = Wave()
