import pygame
from constants import SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_speed = 0

    def update(self):
        self.rect.y += self.y_speed
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
