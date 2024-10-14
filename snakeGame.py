# snake_game.py

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set block size and speed
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Create a clock object to control the speed of the game
clock = pygame.time.Clock()

# Display the score on the screen
def show_score(score):
    font = pygame.font.SysFont("arial", 25)
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, [10, 10])

# Game over message
def game_over():
    font = pygame.font.SysFont("arial", 50)
    msg = font.render("Game Over!", True, RED)
    screen.blit(msg, [WIDTH // 4, HEIGHT // 3])
    pygame.display.flip()
    time.sleep(2)  # Wait for 2 seconds before closing the game

# Main game loop
def game_loop():
    # Initial snake settings
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = "RIGHT"
    change_to = direction

    # Random initial food position
    food_pos = [random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
    food_spawn = True

    score = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        # Update direction
        direction = change_to

        # Move the snake
        if direction == "UP":
            snake_pos[1] -= BLOCK_SIZE
        elif direction == "DOWN":
            snake_pos[1] += BLOCK_SIZE
        elif direction == "LEFT":
            snake_pos[0] -= BLOCK_SIZE
        elif direction == "RIGHT":
            snake_pos[0] += BLOCK_SIZE

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        # Spawn new food
        if not food_spawn:
            food_pos = [random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
        food_spawn = True

        # Clear screen
        screen.fill(BLACK)

        # Draw the snake
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw the food
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # Check if the snake hits the boundaries or itself
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
            snake_pos in snake_body[1:]):
            game_over()
            return

        # Show score
        show_score(score)

        # Update the display
        pygame.display.update()

        # Control the speed of the snake
        clock.tick(SNAKE_SPEED)

# Start the game
if __name__ == "__main__":
    game_loop()
