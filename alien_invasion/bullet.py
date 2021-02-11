import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, sets, scr, ship):
        super().__init__()
        self.screen = scr

        self.rect = pygame.Rect(0, 0, sets.bullet_width, sets.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = sets.bullet_color
        self.speed = sets.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
