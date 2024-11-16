import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up the window dimensions
window_x = 600
window_y = 400

# Create the game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# Define colors
black = pygame.Color(0, 0, 0)       # Background
white = pygame.Color(255, 255, 255) # Score
red = pygame.Color(255, 0, 0)       # Food
green = pygame.Color(0, 255, 0)     # Snake
gray = pygame.Color(128, 128, 128)  # Walls

# Set the game clock
fps = pygame.time.Clock()

# Snake speed
snake_speed = 15

# Snake default position
snake_position = [100, 50]

# Initial snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50]]

# Initial food position
food_position = [random.randrange(1, (window_x//10)) * 10,
                 random.randrange(1, (window_y//10)) * 10]
food_spawn = True

# Set default direction
direction = 'RIGHT'
change_to = direction

# Initialize score
score = 0

# Define walls for level 2
walls = [
    pygame.Rect(200, 100, 200, 10),  # Horizontal wall
    pygame.Rect(200, 290, 200, 10),  # Horizontal wall
    pygame.Rect(200, 100, 10, 200),  # Vertical wall
    pygame.Rect(390, 100, 10, 200)   # Vertical wall
]

# Game Over function
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    GO_surface = font.render('Game Over', True, red)
    GO_rect = GO_surface.get_rect()
    GO_rect.midtop = (window_x/2, window_y/4)
    game_window.fill(black)
    game_window.blit(GO_surface, GO_rect)
    show_score(0)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Display Score
def show_score(choice=1):
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Score : ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.topleft = (10, 10)
    else:
        score_rect.midtop = (window_x/2, window_y/1.25)
    game_window.blit(score_surface, score_rect)

# Main Function
def game_loop(level=1):
    global snake_speed, direction, change_to, score, food_spawn
    while True:
        # Handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'

        # Validate direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position == food_position:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawn food
        if not food_spawn:
            food_position = [random.randrange(1, (window_x//10)) * 10,
                             random.randrange(1, (window_y//10)) * 10]
        food_spawn = True

        # Fill background
        game_window.fill(black)

        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw food
        pygame.draw.rect(game_window, red, pygame.Rect(
            food_position[0], food_position[1], 10, 10))

        # Level 2 walls
        if level == 2:
            for wall in walls:
                pygame.draw.rect(game_window, gray, wall)
            # Check collision with walls
            for wall in walls:
                if wall.collidepoint(snake_position[0], snake_position[1]):
                    game_over()

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        # Check collision with self
        for block in snake_body[1:]:
            if snake_position == block:
                game_over()

        # Display score
        show_score()

        # Refresh game screen
        pygame.display.update()

        # Set the speed
        fps.tick(snake_speed)

# Start the game
if __name__ == "__main__":
    # Level selection
    level = 1  # Change to 2 for level with walls
    game_loop(level)
