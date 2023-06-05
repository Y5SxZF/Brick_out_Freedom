# game_logic.py
from paddle import Paddle
from ball import Ball
from brick import Bricks
from config import SCREEN_HEIGHT,SCREEN_WIDTH
import pygame
from levels import LEVELS
import sys

from config import *
background_image = pygame.image.load('res/img/background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.init()

brick_hit_sound = pygame.mixer.Sound('res/snd/brick_hit.mp3')
brick_break_sound = pygame.mixer.Sound('res/snd/brick_break.mp3')

class Lives:
    def __init__(self, total_lives):
        self.total_lives = total_lives
        self.life_images = [pygame.transform.scale(pygame.image.load("res/img/life.png"), (30,30)),
                            pygame.transform.scale(pygame.image.load("res/img/life_half.png"), (30,30)), 
                            pygame.transform.scale(pygame.image.load("res/img/life_all_gone.png"), (30,30))]
        self.current_image_index = 0  # index of current image

    def lose_life(self):
        if self.total_lives > 0:
            self.total_lives -= 1
            self.current_image_index += 1

    def draw(self, screen):
        if self.total_lives > 0:
            screen.blit(self.life_images[self.current_image_index], (SCREEN_WIDTH-30, 0))


class Game:
    def __init__(self, ball_speed, paddle_width):
        self.ball = Ball(ball_speed)
        self.paddle = Paddle(paddle_width)
        self.clock = pygame.time.Clock()
        self.lives = Lives(3)
        self.lives = 3
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.current_level = 0
        self.load_level()

    def load_level(self):
        # Check if there is a next level
        if self.current_level < len(LEVELS):
            self.bricks = Bricks(LEVELS[self.current_level])
            self.lives = Lives(3)
        else:
            print("You have completed all levels!")
            pygame.quit()
            sys.exit()

    def update(self):
        # Other game updates...
        self.check_bricks()

    def check_bricks(self):
        # Check if all bricks are destroyed
        for brick in self.bricks.bricks:
            if brick.hits_remaining == 0:
                self.bricks.bricks.remove(brick)

        if len(self.bricks.bricks) == 0:
            self.current_level += 1
            self.load_level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            self.paddle.move_paddle()
            self.ball.move_ball()

            if self.ball.ball.bottom > SCREEN_HEIGHT:
                self.lives.lose_life()
                if self.lives.total_lives == 0:
                    print("Game Over")
                    return False
                else:
                    self.ball.reset_ball()

            if self.ball.ball.colliderect(self.paddle.paddle):
                self.ball.bounce()

            for brick in self.bricks.bricks:
                if self.ball.ball.colliderect(brick.rect):
                    self.ball.bounce()
                    brick.hits_remaining -= 1
                    if brick.hits_remaining == 0:
                      self.bricks.bricks.remove(brick)
                      brick_break_sound.play()
                    else :
                        brick_hit_sound.play()

            self.screen.fill((0, 0, 0))
            screen.blit(background_image, (0, 0))
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.bricks.draw(self.screen)
            self.lives.draw(self.screen)

            self.update()

            pygame.display.flip()
            self.clock.tick(FPS)
        return True