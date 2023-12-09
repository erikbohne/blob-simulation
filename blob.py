import random
import pygame
import math
from utils import Config

config = Config()

#####################
# Blue Blob - Prey
#####################

class BlueBlob:

    def __init__(self, x_boundary, y_boundary, speed=None, size=None, energy=None):
        self.x = random.uniform(0, x_boundary)
        self.y = random.uniform(0, y_boundary)
        self.size = size if size is not None else random.uniform(4.0, 8.0)

        # Speed is inversely related to size (larger blobs are slower)
        self.speed = speed if speed is not None else 2.0 - (self.size - 4.0) * 0.25
        self.speed = max(0.5, min(self.speed, 2.0))  # Ensure speed stays within reasonable bounds

        self.energy = energy if energy is not None else 100 + (self.size - 4.0) * 25
        self.energy_consumption = self.speed * 0.5  # Faster blobs consume more energy

    def move(self, foods):
        if not foods:
            return
        nearest_food = min(foods, key=lambda food: self.distance_to(food))
        if self.distance_to(nearest_food) <= self.size:
            self.eat(nearest_food.energy)
            foods.remove(nearest_food)
        else:
            self.x += self.speed if nearest_food.x > self.x else -self.speed
            self.y += self.speed if nearest_food.y > self.y else -self.speed
            self.energy -= 1  # Adjust energy cost as needed

    def eat(self, food_amount):
        self.energy += food_amount

    def reproduce(self, env):
        if self.energy > config.reproduction_threshold:
            # Variation in size for offspring
            offspring_size = self.size + random.uniform(-0.5, 0.5)
            offspring_size = max(4, min(offspring_size, 8))

            # Speed adjusted based on size
            offspring_speed = 2.0 - (offspring_size - 4.0) * 0.25

            # New energy for offspring with some variation
            offspring_energy = self.energy / 2

            new_blob = BlueBlob(self.x, self.y, speed=offspring_speed, size=offspring_size, energy=offspring_energy)
            env.blobs.append(new_blob)
            self.energy /= 2  # Parent loses energy after reproduction
            
    def survive(self, env):
        if self.energy < 0:
            env.blobs.remove(self)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), self.size)


#####################
#  Red Blob - Predator
#####################

class RedBlob:

    def __init__(self, x_boundary, y_boundary):
        self.x = random.randint(0, x_boundary)
        self.y = random.randint(0, y_boundary)
        self.size = random.randint(6, 10)  # Generally bigger than BlueBlob
        self.energy = 150  # Higher initial energy

    def move(self, foods):
        self.x += random.randint(-2, 2)  # Moves faster
        self.y += random.randint(-2, 2)
        self.energy -= 2  # Moving costs more energy due to bigger size

    def hunt(self, prey):
        # Logic for hunting BlueBlobs
        pass

    def reproduce(self):
        # Reproduction logic, similar to BlueBlob but maybe different criteria
        pass
    
    def draw(self, screen):
        # Draw the RedBlob on the screen
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size)