import pygame
from utils import Config

class Environment:
    def __init__(self):
        self.config = Config()

        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((self.config.x_boundary, self.config.y_boundary))
        pygame.display.set_caption("Blob World Simulation")

        # Set up a clock for managing the frame rate
        self.clock = pygame.time.Clock()

    def run(self, update_function, draw_function):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update the environment and entities
            update_function()

            # Draw everything
            self.screen.fill((255, 255, 255))  # Clear the screen with a white background
            draw_function(self.screen)

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)  # 60 frames per second

        pygame.quit()
