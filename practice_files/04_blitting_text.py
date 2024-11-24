import pygame
import os

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

#Define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

#See all available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

#Define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font_loc = os.path.join('practice_files', '04_font', 'AnkhSanctuary-PVK0B.ttf')
custom_font = pygame.font.Font(custom_font_loc, 32)

#Define texts
system_text = system_font.render("ALIEN INVADER!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("There is no escape!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Blit (copy) the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()

