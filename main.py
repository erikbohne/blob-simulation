from blob import BlueBlob, RedBlob
from environment import Environment
from simulation import update, draw
from utils import Config

# Initialize the config
config = Config()

# Initialize the environment and blobs
env = Environment()
BlueBlobs = [BlueBlob(config.x_boundary, config.y_boundary) for i in range(10)]
RedBlobs = [RedBlob(config.x_boundary, config.y_boundary) for i in range(10)]
blobs = BlueBlobs + RedBlobs

# Start the simulation
env.run(lambda: update(blobs), lambda screen: draw(blobs, screen))

