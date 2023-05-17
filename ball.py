# ball.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_DIAMETER, WHITE

class Ball:
    def __init__(self):
        self.ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_DIAMETER, BALL_DIAMETER)
        self.speed = [4, -4]

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.ball)

    def move(self):
        self.ball.move_ip(*self.speed)

    def check_collision(self):
        if self.ball.left < 0 or self.ball.right > SCREEN_WIDTH:
            self.speed[0] *= -1
        if self.ball.top < 0:
            self.speed[1] *= -1
