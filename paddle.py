# paddle.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE

class Paddle:
    def __init__(self):
        self.paddle = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.paddle)

    def move(self, direction):
        self.paddle.move_ip(direction, 0)
        if self.paddle.left < 0:
            self.paddle.left = 0
        if self.paddle.right > SCREEN_WIDTH:
            self.paddle.right = SCREEN_WIDTH
