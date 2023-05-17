# brick.py
import pygame
from config import SCREEN_WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BLUE

class Brick:
    def __init__(self, pos_x, pos_y):
        self.brick = pygame.Rect(pos_x, pos_y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.brick)

class Bricks:
    def __init__(self):
        self.bricks = [Brick(i*(BRICK_WIDTH+2), j*(BRICK_HEIGHT+2)) for i in range(SCREEN_WIDTH // (BRICK_WIDTH+2)) for j in range(5)]

    def draw(self, screen):
        for brick in self.bricks:
            brick.draw(screen)
