# game_logic.py
from paddle import Paddle
from ball import Ball
from brick import Bricks
from config import SCREEN_HEIGHT,SCREEN_WIDTH
import pygame
from config import *
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Game:
    def __init__(self, ball_speed, paddle_width):
        self.ball = Ball(ball_speed)
        self.paddle = Paddle(paddle_width)
        self.bricks = Bricks()

        self.lives = 3

    def ball_hits_paddle(self):
        if self.ball.ball.colliderect(self.paddle.paddle):
            self.ball.speed[1] *= -1

    def ball_hits_brick(self):
        for brick in self.bricks.bricks[:]:
            if self.ball.ball.colliderect(brick.brick):
                self.ball.speed[1] *= -1
                self.bricks.bricks.remove(brick)

    def ball_hits_bottom(self):
        if self.ball.ball.bottom > SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives == 0:
                print("Game Over")
                return False
            else:
                self.ball.ball.left, self.ball.ball.top = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
                self.ball.speed[1] *= -1
        return True

    def run(self):
        self.ball.move()
        self.ball.check_collision()
        self.ball_hits_paddle()
        self.ball_hits_brick()
        return self.ball_hits_bottom()


class Game:
    def __init__(self, ball_speed, paddle_width):
        self.ball = Ball(ball_speed)
        self.paddle = Paddle(paddle_width)
        brick_layout = [
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0],
  [0, 0, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 0, 0, 0],
  [0, 1, 2, 3, 0, 0, 0, 2, 0, 0, 0, 3, 2, 1, 0],
  [1, 2, 3, 0, 0, 2, 3, 1, 3, 2, 0, 0, 3, 2, 1],
  [0, 1, 2, 3, 0, 0, 0, 2, 0, 0, 0, 3, 2, 1, 0],
  [0, 0, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 0, 0, 0],
  [0, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
        self.bricks = Bricks(brick_layout)
        self.clock = pygame.time.Clock()
        self.lives = 3
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

            if self.bricks.collide(self.ball.ball):
                self.ball.bounce()

            self.screen.fill((0, 0, 0))
            screen.blit(background_image, (0, 0))
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.bricks.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)
        return True
