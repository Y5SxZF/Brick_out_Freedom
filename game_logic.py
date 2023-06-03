# game_logic.py
from paddle import Paddle
from ball import Ball
from brick import Bricks
from config import SCREEN_HEIGHT,SCREEN_WIDTH
import pygame
from levels import LEVELS
import sys

from config import *
background_image = pygame.image.load('res/img/background.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.init()

brick_hit_sound = pygame.mixer.Sound('res/snd/brick_hit.mp3')
brick_break_sound = pygame.mixer.Sound('res/snd/brick_break.mp3')

class Game:
    def __init__(self, ball_speed, paddle_width):
        self.ball = Ball(ball_speed)
        self.paddle = Paddle(paddle_width)
        self.clock = pygame.time.Clock()
        self.lives = 3
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.current_level = 0
        self.load_level()

    def load_level(self):
        # Check if there is a next level
        if self.current_level < len(LEVELS):
            self.bricks = Bricks(LEVELS[self.current_level])
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
                self.lives -= 1
                if self.lives == 0:
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

            self.update()

            pygame.display.flip()
            self.clock.tick(FPS)
        return True