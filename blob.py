import random
import pygame
import math

#####################
# Blue Blob - Prey
#####################

class BlueBlob:

    def __init__(self, x_boundary, y_boundary):
        self.x = random.randint(0, x_boundary)
        self.y = random.randint(0, y_boundary)
        self.speed = random.randint(1,2)
        self.size = random.randint(4, 8)
        self.energy = 100  # Initial energy

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

    def reproduce(self):
        # Reproduction logic here, if energy is high enough, create a new BlueBlob
        pass

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