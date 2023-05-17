# main.py
import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game_logic import Game

# Initialize Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Initialize the game
game = Game()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game.paddle.move(-7)
    if keys[pygame.K_RIGHT]:
        game.paddle.move(7)

    # Move the ball
    game.ball.move()

    # Check ball collision
    game.ball.check_collision()

    # Game logic for ball hitting the bottom, bouncing off the paddle, and hitting bricks would go here
    # For now, we will just draw everything

    # Draw everything
    screen.fill((0, 0, 0))  # Fill the screen with black
    game.bricks.draw(screen)  # Draw bricks
    game.paddle.draw(screen)  # Draw the paddle
    game.ball.draw(screen)  # Draw the ball

    pygame.display.flip()  # Update the display

    clock.tick(FPS)  # Cap the frame rate
    game_running = game.run()
    if not game_running:
        pygame.quit()
        sys.exit()