import pygame
import random
from constants import *
from game.paddle import Paddle
from game.ball import Ball

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()
balls = pygame.sprite.Group()

player_paddle = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
computer_paddle = Paddle(SCREEN_WIDTH - PADDLE_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2)

all_sprites.add(player_paddle, computer_paddle, ball)
paddles.add(player_paddle, computer_paddle)
balls.add(ball)
pygame.display.set_caption('Hoopa')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_paddle.y_speed = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                player_paddle.y_speed = PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_paddle.y_speed = 0

    if ball.rect.centery < computer_paddle.rect.centery:
        if random.random() < 0.7:
            computer_paddle.y_speed = -PADDLE_SPEED
        else:
            computer_paddle.y_speed = 0
    elif ball.rect.centery > computer_paddle.rect.centery:
        if random.random() < 0.7:
            computer_paddle.y_speed = PADDLE_SPEED
        else:
            computer_paddle.y_speed = 0
    else:
        computer_paddle.y_speed = 0

    all_sprites.update()

    if pygame.sprite.spritecollide(player_paddle, balls, False) or pygame.sprite.spritecollide(computer_paddle, balls, False):
        ball.x_speed *= -1

    if ball.rect.left < 0 or ball.rect.right > SCREEN_WIDTH:
        running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()