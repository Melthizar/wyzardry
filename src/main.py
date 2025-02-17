import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)
BACKGROUND_COLOR = (0, 0, 0)  # Black
GRID_COLOR = (50, 50, 50)    # Dark Gray
PLAYER_COLOR = (0, 255, 0)   # Green

# Create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Wyzardry")

def draw_grid(surface, cell_size=50):
    """Draw a grid on the surface"""
    for x in range(0, WINDOW_SIZE[0], cell_size):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, WINDOW_SIZE[1]))
    for y in range(0, WINDOW_SIZE[1], cell_size):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (WINDOW_SIZE[0], y))

def draw_player(surface, pos, size=40):
    """Draw a simple square player"""
    rect = pygame.Rect(pos[0] - size//2, pos[1] - size//2, size, size)
    pygame.draw.rect(surface, PLAYER_COLOR, rect)

# Main game loop
def main():
    player_pos = [WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2]  # Center of screen
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill screen with background color
        screen.fill(BACKGROUND_COLOR)
        
        # Draw grid and player
        draw_grid(screen)
        draw_player(screen, player_pos)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()