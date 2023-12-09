import random

class Food:
    def __init__(self, x_boundary, y_boundary):
        self.x = random.randint(0, x_boundary)
        self.y = random.randint(0, y_boundary)
        self.energy = 20  # or any value you deem appropriate
