import pygame
import time
import random

pygame.font.init() # initialize font module

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

BG = pygame.transform.scale(pygame.image.load('bg.jpeg'), (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60 
PLAYER_VEL = 5

FONT = pygame.font.SysFont('comicsans', 30)

def draw(player, ellapsed_time):
    # blit is used to draw an image or surface to screen
    WIN.blit(BG, (0, 0)) # (image, (coordinate to place top left corner of image))

    time_text = FONT.render(f"Time: {round(ellapsed_time)}s", 1, (255, 255, 255)) # (text (Round off the time), antialiasing, color) Color - str or rgb
    WIN.blit(time_text, (10, 10)) # (text, (coordinate to place top left corner of text))

    # (surface, color, rect) where color = string or (r, g, b)
    pygame.draw.rect(WIN, (255, 0, 0), player)

    pygame.display.update()

def main():
    run = True

    # (x, y, width, height)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    ellapsed_time = 0

    while run:
        clock.tick(60) # 60 fps for this while loop
        ellapsed_time = time.time() - start_time # time since start of game

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

        draw(player, ellapsed_time)

    pygame.quit()


# since we want to run the game only when this file is run and now when say it is imported``
if __name__ == "__main__":
    main()
# https://www.youtube.com/watch?v=waY3LfJhQLY   time : 27:08