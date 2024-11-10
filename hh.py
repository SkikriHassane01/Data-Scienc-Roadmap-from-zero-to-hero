import pygame
import sys
import random
import json
from datetime import datetime
from pathlib import Path

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 168, 82)
RED = (255, 0, 0)
DARK_GREEN = (34, 120, 57)
GRAY = (128, 128, 128)

# Game Settings
FPS = 60
SNAKE_SPEED = 15
GAME_TITLE = "Python Snake Adventure"

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, 36)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=12)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset_game()
        self.load_history()
        
        # Create buttons
        self.start_button = Button(300, 250, 200, 50, "Start Game", GREEN)
        self.history_button = Button(300, 320, 200, 50, "History", DARK_GREEN)
        
    def reset_game(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        
    def spawn_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH-1), 
                   random.randint(0, GRID_HEIGHT-1))
            if food not in self.snake:
                return food
                
    def load_history(self):
        self.history_file = Path("snake_history.json")
        if self.history_file.exists():
            with open(self.history_file) as f:
                self.history = json.load(f)
        else:
            self.history = []
            
    def save_history(self):
        game_record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "score": self.score
        }
        self.history.append(game_record)
        self.history.sort(key=lambda x: x["score"], reverse=True)
        self.history = self.history[:10]  # Keep only top 10 scores
        
        with open(self.history_file, "w") as f:
            json.dump(self.history, f)
            
    def draw_menu(self):
        self.screen.fill(BLACK)
        
        # Draw title
        title = self.font.render(GAME_TITLE, True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 150))
        self.screen.blit(title, title_rect)
        
        # Draw buttons
        self.start_button.draw(self.screen)
        self.history_button.draw(self.screen)
        
    def draw_history(self):
        self.screen.fill(BLACK)
        
        # Draw title
        title = self.font.render("High Scores", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 50))
        self.screen.blit(title, title_rect)
        
        # Draw history entries
        for i, entry in enumerate(self.history):
            text = f"{i+1}. Score: {entry['score']} - {entry['date']}"
            score_text = self.font.render(text, True, WHITE)
            self.screen.blit(score_text, (50, 100 + i * 40))
            
        # Back button
        back_button = Button(300, 500, 200, 50, "Back", GRAY)
        back_button.draw(self.screen)
        return back_button
        
    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw snake
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN,
                           (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE,
                            GRID_SIZE-2, GRID_SIZE-2))
            
        # Draw food
        pygame.draw.rect(self.screen, RED,
                        (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE,
                         GRID_SIZE-2, GRID_SIZE-2))
                         
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press SPACE to restart",
                                            True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2,
                                                       WINDOW_HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
            
    def update(self):
        if self.game_over:
            return
            
        # Move snake
        head = self.snake[0]
        new_head = ((head[0] + self.direction[0]) % GRID_WIDTH,
                   (head[1] + self.direction[1]) % GRID_HEIGHT)
        
        # Check collision with self
        if new_head in self.snake:
            self.game_over = True
            self.save_history()
            return
            
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()
            
    def run(self):
        state = "MENU"  # MENU, GAME, HISTORY
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if state == "MENU":
                        if self.start_button.is_clicked(event.pos):
                            state = "GAME"
                            self.reset_game()
                        elif self.history_button.is_clicked(event.pos):
                            state = "HISTORY"
                    elif state == "HISTORY":
                        back_button = Button(300, 500, 200, 50, "Back", GRAY)
                        if back_button.is_clicked(event.pos):
                            state = "MENU"
                            
                if event.type == pygame.KEYDOWN:
                    if state == "GAME":
                        if not self.game_over:
                            if event.key == pygame.K_UP and self.direction != (0, 1):
                                self.direction = (0, -1)
                            elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                                self.direction = (0, 1)
                            elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                                self.direction = (-1, 0)
                            elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                                self.direction = (1, 0)
                        elif event.key == pygame.K_SPACE:
                            self.reset_game()
                            
            if state == "MENU":
                self.draw_menu()
            elif state == "GAME":
                self.update()
                self.draw_game()
            elif state == "HISTORY":
                self.draw_history()
                
            pygame.display.flip()
            self.clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    game = Game()
    game.run()