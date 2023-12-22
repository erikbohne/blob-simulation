class Config:
    def __init__(self):
        
        # Boundaries
        self.x_boundary = 800
        self.y_boundary = 600

        # Colors
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        
        # Parameters
        self.reproduction_threshold = 200
        self.food_energy = 50
        self.food_amount = 200
        
        # Starting blobs
        self.starting_blue_blobs = 10
        self.starting_red_blobs = 0