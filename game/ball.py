import pygame
from constants import SCREEN_HEIGHT, BALL_WIDTH, BALL_HEIGHT, BALL_X_SPEED, BALL_Y_SPEED

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BALL_WIDTH, BALL_HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = BALL_X_SPEED
        self.y_speed = BALL_Y_SPEED

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.y_speed = -self.y_speed
