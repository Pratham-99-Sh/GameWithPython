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
STAR_WIDTH, STAR_HEIGHT = 10, 20
STAR_VEL = 3

FONT = pygame.font.SysFont('comicsans', 30)

def draw(player, ellapsed_time, stars):
    # blit is used to draw an image or surface to screen
    WIN.blit(BG, (0, 0)) # (image, (coordinate to place top left corner of image))

    time_text = FONT.render(f"Time: {round(ellapsed_time)}s", 1, (255, 255, 255)) # (text (Round off the time), antialiasing, color) Color - str or rgb
    WIN.blit(time_text, (10, 10)) # (text, (coordinate to place top left corner of text))

    # (surface, color, rect) where color = string or (r, g, b)
    pygame.draw.rect(WIN, (255, 0, 0), player)

    # we did it after player to make stars appear above player
    for star in stars:
        pygame.draw.rect(WIN, (0, 255, 0), star)

    pygame.display.update()

def main():
    run = True

    # (x, y, width, height)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    ellapsed_time = 0

    star_add_increment = 2000 # in milliseconds
    star_count = 0 # variable to tell us when to add next star

    stars = [] # list of all stars
    hit = False

    while run:
        star_count += clock.tick(60) # 60 fps for this while loop and it returns the time since the last tick
        ellapsed_time = time.time() - start_time # time since start of game

        if star_count >= star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) # (x, y, width, height) where y is - ve so that it starts above the screen
                stars.append(star)

            star_count = 0
            star_add_increment = max(200, star_add_increment - 50) # decrease the time to add next star by 100ms

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

        for star in stars[:]:
            star.y += STAR_VEL 
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player): # only chekck for colliosn if the star is below the player
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, (255, 255, 255))
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, ellapsed_time, stars)

    pygame.quit()


# since we want to run the game only when this file is run and now when say it is imported``
if __name__ == "__main__":
    main()