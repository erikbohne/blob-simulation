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
        BlueBlobs = [BlueBlob(self.config.x_boundary, self.config.y_boundary) for i in range(config.starting_blue_blobs)]
        RedBlobs = [RedBlob(self.config.x_boundary, self.config.y_boundary) for i in range(config.starting_red_blobs)]
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
        
        # Calculate average speed
        blue_speeds = [blob.speed for blob in self.blobs if isinstance(blob, BlueBlob)]
        red_speeds = [blob.speed for blob in self.blobs if isinstance(blob, RedBlob)]
        average_blue_speed = np.mean(blue_speeds) if blue_speeds else 0
        average_red_speed = np.mean(red_speeds) if red_speeds else 0
        
        # Calculate average size
        blue_sizes = [blob.size for blob in self.blobs if isinstance(blob, BlueBlob)]
        red_sizes = [blob.size for blob in self.blobs if isinstance(blob, RedBlob)]
        average_blue_size = np.mean(blue_sizes) if blue_sizes else 0
        average_red_size = np.mean(red_sizes) if red_sizes else 0
        
        # Calculate total energy
        total_energy = sum(blob.energy for blob in self.blobs)
        
        text = font.render(f'Blue Blobs: {blue_count}, Red Blobs: {red_count}', True, (0, 0, 0))
        self.screen.blit(text, (10, 10))  # Position the text on the screen
        
        text = font.render(f'Average Blue Speed: {average_blue_speed:.2f}', True, (0, 0, 0))
        self.screen.blit(text, (10, 40))
        
        text = font.render(f'Average Red Speed: {average_red_speed:.2f}', True, (0, 0, 0))
        self.screen.blit(text, (10, 70))
        
        text = font.render(f'Average Blue Size: {average_blue_size:.2f}', True, (0, 0, 0))
        self.screen.blit(text, (10, 100))
        
        text = font.render(f'Average Red Size: {average_red_size:.2f}', True, (0, 0, 0))
        self.screen.blit(text, (10, 130))
        
        text = font.render(f'Total Energy: {total_energy}', True, (0, 0, 0))
        self.screen.blit(text, (10, 160))

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
