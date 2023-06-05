# brick.py
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT
import pygame

class Brick:
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
        black_brick_images = [pygame.transform.scale(pygame.image.load("res/img/black.png"), (BRICK_WIDTH, BRICK_HEIGHT))]

        brown_brick_images = [pygame.transform.scale(pygame.image.load("res/img/brown.png"), (BRICK_WIDTH, BRICK_HEIGHT))]

        pink_brick_images = [pygame.transform.scale(pygame.image.load("res/img/pink.png"), (BRICK_WIDTH, BRICK_HEIGHT))]

        blue_brick_images = [pygame.transform.scale(pygame.image.load("res/img/blue_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/blue.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        
        green_brick_images = [pygame.transform.scale(pygame.image.load("res/img/green_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/green.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        
        red1_brick_images = [pygame.transform.scale(pygame.image.load("res/img/red1_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/red1.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        
        red2_brick_images = [pygame.transform.scale(pygame.image.load("res/img/red2_cracked_twice.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/red2_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/red2.png"), (BRICK_WIDTH, BRICK_HEIGHT))]
        
        white_brick_images = [pygame.transform.scale(pygame.image.load("res/img/white_cracked_twice.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/white_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/white.png"), (BRICK_WIDTH, BRICK_HEIGHT))]

        yellow_brick_images = [pygame.transform.scale(pygame.image.load("res/img/yellow_cracked_twice.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/yellow_cracked_once.png"), (BRICK_WIDTH, BRICK_HEIGHT)), 
                           pygame.transform.scale(pygame.image.load("res/img/yellow.png"), (BRICK_WIDTH, BRICK_HEIGHT))]    
            
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                rect = pygame.Rect(j*(BRICK_WIDTH+2), i*(BRICK_HEIGHT+2), BRICK_WIDTH, BRICK_HEIGHT)
                if layout[i][j] == 1:
                    self.bricks.append(Brick('yellow', 3, rect, yellow_brick_images))
                elif layout[i][j] == 2:
                    self.bricks.append(Brick('blue', 2, rect, blue_brick_images))
                elif layout[i][j] == 3:
                    self.bricks.append(Brick('black', 1, rect, black_brick_images))
                elif layout[i][j] == 4:
                    self.bricks.append(Brick('white', 3, rect, white_brick_images))
                elif layout[i][j] == 5:
                    self.bricks.append(Brick('green', 2, rect, green_brick_images))
                elif layout[i][j] == 6:
                    self.bricks.append(Brick('brown', 1, rect, brown_brick_images))
                elif layout[i][j] == 7:
                    self.bricks.append(Brick('red2', 3, rect, red2_brick_images))
                elif layout[i][j] == 8:
                    self.bricks.append(Brick('red1', 2, rect, red1_brick_images))
                elif layout[i][j] == 9:
                    self.bricks.append(Brick('pink', 1, rect, pink_brick_images))

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
                return True
        return False

    def remove_destroyed_bricks(self):
        self.bricks = [brick for brick in self.bricks if brick.hits_remaining > 0]