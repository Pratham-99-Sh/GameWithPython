import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

BG = pygame.transform.scale(pygame.image.load('bg.jpeg'), (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60 
PLAYER_VEL = 5

def draw(player):
    # blit is used to draw an image or surface to screen
    WIN.blit(BG, (0, 0)) # (image, (coordinate to place top left corner of image))

    # (surface, color, rect) where color = string or (r, g, b)
    pygame.draw.rect(WIN, (255, 0, 0), player)

    pygame.display.update()

def main():
    run = True

    # (x, y, width, height)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60) # 60 fps for this while loop
        # pygame.event.get() returns a list of all the events that have happened since the last time it was called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()


# since we want to run the game only when this file is run and now when say it is imported``
if __name__ == "__main__":
    main()