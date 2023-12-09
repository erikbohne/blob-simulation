import pygame
import numpy as np
from utils import Config
from food import Food
from blob import BlueBlob, RedBlob
from data_analysis import DataAnalysis

config = Config()
class Environment:
    def __init__(self):
        self.config = Config()
        self.foods = [Food(self.config.x_boundary, self.config.y_boundary) for _ in range(10)]

        # Initialize the blobs
        BlueBlobs = [BlueBlob(self.config.x_boundary, self.config.y_boundary) for i in range(10)]
        RedBlobs = [RedBlob(self.config.x_boundary, self.config.y_boundary) for i in range(0)]
        self.blobs = BlueBlobs + RedBlobs
        
        # Initialize the data analysis
        self.data_analysis = DataAnalysis()
        
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((self.config.x_boundary, self.config.y_boundary))
        pygame.display.set_caption("Blob World Simulation")

        # Set up a clock for managing the frame rate
        self.clock = pygame.time.Clock()
        
    def draw_status(self):
        font = pygame.font.SysFont(None, 24)  # You can choose a different font or size
        blue_count = sum(isinstance(blob, BlueBlob) for blob in self.blobs)
        red_count = sum(isinstance(blob, RedBlob) for blob in self.blobs)
        text = font.render(f'Blue Blobs: {blue_count}, Red Blobs: {red_count}', True, (0, 0, 0))
        self.screen.blit(text, (10, 10))  # Position the text on the screen

    def run(self, update_function, draw_function):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            # Add new food
            if len(self.foods) < config.food_amount:
                self.foods.append(Food(self.config.x_boundary, self.config.y_boundary))
                
            # Update Data Analysis
            self.data_analysis.collect_data(self.blobs)

            # Update the environment and entities
            update_function(self.blobs, self.foods, self)

            # Draw everything
            self.screen.fill((255, 255, 255))  # Clear the screen
            draw_function(self.blobs, self.foods, self.screen)  # Draw blobs and foods
            self.data_analysis.draw_graph(self.screen)  # Draw the data graph
            self.draw_status()  # Draw status information

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)  # 60 frames per second

        pygame.quit()
