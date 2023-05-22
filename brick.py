# brick.py
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BLUE, RED, GREEN
import pygame

class Brick:
    def __init__(self, x, y, color, hits):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.hits_remaining = hits

class Bricks:
    def __init__(self, layout):
        self.bricks = []
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == 1:
                    self.bricks.append(Brick(j*(BRICK_WIDTH+2), i*(BRICK_HEIGHT+2), BLUE, 1))
                elif layout[i][j] == 2:
                    self.bricks.append(Brick(j*(BRICK_WIDTH+2), i*(BRICK_HEIGHT+2), RED, 2))
                elif layout[i][j] == 3:
                    self.bricks.append(Brick(j*(BRICK_WIDTH+2), i*(BRICK_HEIGHT+2), GREEN, 3))

    def draw(self, screen):
        for brick in self.bricks:
            pygame.draw.rect(screen, brick.color, brick.rect)

    def collide(self, ball):
        for brick in self.bricks:
            if ball.colliderect(brick.rect):
                brick.hits_remaining -= 1
                if brick.hits_remaining == 0:
                    self.bricks.remove(brick)
                return True
        return False
