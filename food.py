import random
import pygame
class Food:
    def __init__(self, x_boundary, y_boundary):
        self.x = random.randint(0, x_boundary)
        self.y = random.randint(0, y_boundary)
        self.energy = 20  # or any value you deem appropriate

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 5)
        
    def remove(self, foods):
        foods.remove(self)