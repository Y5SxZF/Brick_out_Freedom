# main.py
import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, EASY_SPEED, MODERATE_SPEED, HARD_SPEED, EASY_PADDLE_WIDTH, MODERATE_PADDLE_WIDTH, HARD_PADDLE_WIDTH, WHITE

from game_logic import Game
background_image = pygame.image.load('res/img/background.jpg')
intro_image = pygame.image.load('res/img/intro.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
intro_image = pygame.transform.scale(intro_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
# Initialize Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Function to display the start screen
def start_screen():
    font = pygame.font.Font(None, 36)
    easy_text = font.render("Easy", True, WHITE)
    moderate_text = font.render("Normal", True, WHITE)
    hard_text = font.render("Hard", True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < SCREEN_HEIGHT / 3:
                    return EASY_SPEED, EASY_PADDLE_WIDTH
                elif y < 2 * SCREEN_HEIGHT / 3:
                    return MODERATE_SPEED, MODERATE_PADDLE_WIDTH
                else:
                    return HARD_SPEED, HARD_PADDLE_WIDTH

        screen.blit(intro_image,(0,0))
        screen.blit(easy_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6))
        screen.blit(moderate_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(hard_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 5 / 6))
        pygame.display.flip()
        clock.tick(FPS)
# Start screen
ball_speed, paddle_width = start_screen()

# Initialize the game
game = Game(ball_speed, paddle_width)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game.paddle.move(-10)
    if keys[pygame.K_RIGHT]:
        game.paddle.move(10)


    # Move the ball
    game.ball.move_ball()

    # Check ball collision
    game.ball.check_collision()
    # Game logic for ball hitting the bottom, bouncing off the paddle, and hitting bricks would go here
    # For now, we will just draw everything

    # Draw everything
    # Draw the background
    screen.blit(background_image, (0, 0))    
    game.bricks.draw(screen)  # Draw bricks
    game.paddle.draw(screen)  # Draw the paddle
    game.ball.draw(screen)  # Draw the ball

    pygame.display.flip()  # Update the display

    clock.tick(FPS)  # Cap the frame rate
    game_running = game.run()
    if not game_running:
        pygame.quit()
        sys.exit()

