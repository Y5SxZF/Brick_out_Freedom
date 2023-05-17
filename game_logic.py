# game_logic.py
from paddle import Paddle
from ball import Ball
from brick import Bricks
from config import SCREEN_HEIGHT,SCREEN_WIDTH

class Game:
    def __init__(self):
        self.lives = 3
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()

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
