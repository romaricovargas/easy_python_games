import pygame
import os
import random

#Initialize Pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5

#Load frog image
frog_loc = os.path.join('practice_files', '10_images', 'frog.png')
frog_image = pygame.image.load(frog_loc)
frog_image = pygame.transform.scale(frog_image, (120, 120))
frog_rect = frog_image.get_rect()
frog_rect.topleft = (25, 25)

#Load dragon fly image
dragon_loc = os.path.join('practice_files', '06_images', 'Tiny-Bugs-Dragon-fly.png')
dragon_image = pygame.image.load(dragon_loc)
dragon_image = pygame.transform.scale(dragon_image, (80, 80))
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()
    print(keys)

    #Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and frog_rect.left > 0:
        frog_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and frog_rect.right < WINDOW_WIDTH:
        frog_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and frog_rect.top > 0:
        frog_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and frog_rect.bottom < WINDOW_HEIGHT:
        frog_rect.y += VELOCITY

    #Check for collision between two rects
    if frog_rect.colliderect(dragon_rect):
        print("HIT")
        dragon_rect.x = random.randint(0, WINDOW_WIDTH - 80)
        dragon_rect.y = random.randint(0, WINDOW_HEIGHT - 80)

    #Fill display surface
    display_surface.fill((0, 0, 0))

    #Draw rectanges to represent the rects of each object
    pygame.draw.rect(display_surface, (0, 255, 0), frog_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), dragon_rect, 1)

    #Blit assets
    display_surface.blit(frog_image, frog_rect)
    display_surface.blit(dragon_image, dragon_rect)

    #Update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)
    
#End the game
pygame.quit()
