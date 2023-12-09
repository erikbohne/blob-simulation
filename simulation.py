import pygame

def update(blobs, foods):
    # Update each blob
    for blob in blobs:
        blob.move(foods)

def draw(blobs, foods, screen):
    screen.fill((255, 255, 255))  # Clear the screen with a white background

    # Use the blob's draw method
    for blob in blobs:
        blob.draw(screen)

    # Use the food's draw method
    for food in foods:
        food.draw(screen)
    
    pygame.display.flip()