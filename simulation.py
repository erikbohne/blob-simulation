import pygame

def update(blobs, foods, env):
    # Update each blob
    for blob in blobs:
        blob.move(foods)
        blob.reproduce(env)
        blob.survive(env)

def draw(blobs, foods, screen):
    # Use the blob's draw method
    for blob in blobs:
        blob.draw(screen)

    # Use the food's draw method
    for food in foods:
        food.draw(screen)