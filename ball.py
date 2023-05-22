# ball.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_DIAMETER, WHITE
import random

class Ball:
    def __init__(self, speed):
        # Randomly position the ball at the start along the x-axis
        self.ball = pygame.Rect(random.randint(100, SCREEN_WIDTH - 100), SCREEN_HEIGHT // 2, BALL_DIAMETER, BALL_DIAMETER)
        # Randomly set the x component of the speed and set the y component to always go down towards the paddle
        self.speed = [speed[0] * random.choice([-1, 1]), abs(speed[1])]

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.ball)

    def move_ball(self):
        self.ball.move_ip(self.speed)
        # If ball hits the left or right wall, reverse its direction
        if self.ball.left < 0 or self.ball.right > SCREEN_WIDTH:
            self.speed[0] *= -1
        # If ball hits the top or bottom wall, reverse its direction
        if self.ball.top < 0 or self.ball.bottom > SCREEN_HEIGHT:
            self.speed[1] *= -1

    def reset_ball(self):
        # Randomly set the initial position of the ball and always set the y-component of speed to go down
        self.ball.left, self.ball.top = random.randint(100, SCREEN_WIDTH - 100), SCREEN_HEIGHT // 2
        self.speed = [abs(self.speed[0]) * random.choice([-1, 1]), abs(self.speed[1])]

    def bounce(self):
        self.speed[1] *= -1
    def check_collision(self):
        if self.ball.left < 0 or self.ball.right > SCREEN_WIDTH:
            self.speed[0] *= -1
        if self.ball.top < 0:
            self.speed[1] *= -1
