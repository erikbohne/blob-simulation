import pygame
from utils import Config
from food import Food
from blob import BlueBlob, RedBlob

class Environment:
    def __init__(self):
        self.config = Config()
        self.foods = [Food(self.config.x_boundary, self.config.y_boundary) for _ in range(10)]

        # Initialize the blobs
        BlueBlobs = [BlueBlob(self.config.x_boundary, self.config.y_boundary) for i in range(10)]
        RedBlobs = [RedBlob(self.config.x_boundary, self.config.y_boundary) for i in range(10)]
        self.blobs = BlueBlobs + RedBlobs
        
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
                    
            # Add new food
            if len(self.foods) < 20:
                self.foods.append(Food(self.config.x_boundary, self.config.y_boundary))

            # Update the environment and entities
            update_function(self.blobs, self.foods)

            # Draw everything
            self.screen.fill((255, 255, 255))  # Clear the screen with a white background
            draw_function(self.blobs, self.foods, self.screen)

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)  # 60 frames per second

        pygame.quit()
