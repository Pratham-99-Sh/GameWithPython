import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

BG = pygame.transform.scale(pygame.image.load('bg.jpeg'), (WIDTH, HEIGHT))

def draw():
    # blit is used to draw an image or surface to screen
    WIN.blit(BG, (0, 0)) # (image, (coordinate to place top left corner of image))
    pygame.display.update()

def main():
    run = True

    while run:
        # pygame.event.get() returns a list of all the events that have happened since the last time it was called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()


# since we want to run the game only when this file is run and now when say it is imported``
if __name__ == "__main__":
    main()
    # video tutorial link : https://www.youtube.com/watch?v=waY3LfJhQLY , time : 12:23