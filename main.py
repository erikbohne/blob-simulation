from blob import BlueBlob, RedBlob
from environment import Environment
from simulation import update, draw
from utils import Config

# Initialize the config
config = Config()

# Initialize the environment and blobs
env = Environment()

# Start the simulation
env.run(update, draw)

