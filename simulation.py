from blob import BlueBlob, RedBlob
import pygame

def update(blobs):
    # Update each blob
    for blob in blobs:
        blob.move()

def draw(blobs, screen):
    # Clear the screen (for Pygame, fill it with a background color)
    screen.fill((255, 255, 255))  # White background

    # Draw each blob
    for blob in blobs:
        if isinstance(blob, BlueBlob):
            color = (0, 0, 255)  # Blue for BlueBlob
        elif isinstance(blob, RedBlob):
            color = (255, 0, 0)  # Red for RedBlob

        # Draw the blob as a circle (for Pygame)
        pygame.draw.circle(screen, color, (blob.x, blob.y), blob.size)

    # Update the display to show the new frame (for Pygame)
    pygame.display.flip()
