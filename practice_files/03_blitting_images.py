import pygame
import os

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900
DEFAULT_IMAGE_SIZE = (150, 150)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

#Create images...returns a Surface object with the image drawn on it.
#We can then get the rect of the surface and use the rect to position the image.
space_station_loc = os.path.join('practice_files', '03_images', 'space_station.png')
space_station_image = pygame.image.load(space_station_loc)
space_station_image = pygame.transform.scale(space_station_image, DEFAULT_IMAGE_SIZE)
space_station_rec = space_station_image.get_rect()
space_station_rec.topleft = (0,0)

rocket_loc = os.path.join('practice_files', '03_images', 'rocket.png')
rocket_image = pygame.image.load(rocket_loc)
rocket_image = pygame.transform.scale(rocket_image, DEFAULT_IMAGE_SIZE)
rocket_rec = rocket_image.get_rect()
rocket_rec.topright = (WINDOW_WIDTH,0)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(space_station_image, space_station_rec)
    display_surface.blit(rocket_image, rocket_rec)

    pygame.draw.line(display_surface, (255,255,255), (0,150), (WINDOW_WIDTH, 150))

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()