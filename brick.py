# brick.py
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT
import pygame

class Brick:
    def __init__(self, x, y, hits):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        if hits == 1:
            self.image = pygame.transform.scale(pygame.image.load("blue.png"), (BRICK_WIDTH, BRICK_HEIGHT))
        elif hits == 2:
            self.images = [pygame.transform.scale(pygame.image.load("red_cracked.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("red.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        elif hits == 3:
            self.images = [pygame.transform.scale(pygame.image.load("green_cracked_twice.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("green_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("green.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        self.hits_remaining = hits


    def __init__(self, color, hits_remaining, rect, images):
        self.color = color
        self.hits_remaining = hits_remaining
        self.rect = rect
        self.images = images  # images must be a list of images

    def current_image(self):
        return self.images[self.hits_remaining - 1]

class Bricks:
    def __init__(self, layout):
        self.bricks = []
        blue_brick_images = [pygame.transform.scale(pygame.image.load("blue.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        red_brick_images = [pygame.transform.scale(pygame.image.load("red_cracked.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("red.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        green_brick_images = [pygame.transform.scale(pygame.image.load("green_cracked_twice.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("green_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("green.png"), (BRICK_WIDTH, BRICK_HEIGHT))]

        for i in range(len(layout)):
            for j in range(len(layout[i])):
                rect = pygame.Rect(j*(BRICK_WIDTH+2), i*(BRICK_HEIGHT+2), BRICK_WIDTH, BRICK_HEIGHT)
                if layout[i][j] == 1:
                    self.bricks.append(Brick('blue', 1, rect, blue_brick_images))
                elif layout[i][j] == 2:
                    self.bricks.append(Brick('red', 2, rect, red_brick_images))
                elif layout[i][j] == 3:
                    self.bricks.append(Brick('green', 3, rect, green_brick_images))


    def add_brick(self, brick):
        self.bricks.append(brick)

    def draw(self, screen):
        for brick in self.bricks:
            if brick.hits_remaining > 0:
             screen.blit(brick.current_image(), brick.rect)


    def collide(self, ball):
        for brick in self.bricks:
            if ball.colliderect(brick.rect):
                brick.hits_remaining -= 1
                if brick.hits_remaining == 0:
                    self.bricks.remove(brick)
                return True
        return False
