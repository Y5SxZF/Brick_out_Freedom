# paddle.py
import pygame
from pygame.locals import *
from config import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_HEIGHT, WHITE

class Paddle:
    def __init__(self, width):
        self.paddle = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, width, PADDLE_HEIGHT)
        self.paddle_image = pygame.image.load('res/img/paddle.png')
        self.paddle_image = pygame.transform.scale(self.paddle_image, (width, PADDLE_HEIGHT))

    def draw(self, screen):
        screen.blit(self.paddle_image, self.paddle)

    def move_paddle(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.paddle.move_ip(-7, 0)
        if keys[K_RIGHT]:
            self.paddle.move_ip(7, 0)
        if self.paddle.left < 0:
            self.paddle.left = 0
        if self.paddle.right > SCREEN_WIDTH:
            self.paddle.right = SCREEN_WIDTH