import pygame
import os
import random

#Initialize Pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("You Are What You Eat!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 7
points = 5 

#Set colors
CYAN = (0, 255, 255)
BROWN = (33, 33, 33)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font_loc = os.path.join('you_are_what_you_eat', 'fonts', 'SuperDessert-EaAyj.ttf')
font = pygame.font.Font(font_loc, 32)

#Set Text
score_text = font.render("Score: " + str(points), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("You Are What You Eat", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

timer_text = font.render("99", True, GREEN, DARKGREEN)
timer_rect = timer_text.get_rect()
timer_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Set sounds
food_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'food.wav')
food_sound = pygame.mixer.Sound(food_sound_loc)
poison_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'poison.wav')
poison_sound = pygame.mixer.Sound(poison_sound_loc)
intro_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'intro.wav')
pygame.mixer.music.load(intro_sound_loc)

#set characters image
goodchar_stand_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'good_minion_standing.png')
goodchar_stand_image = pygame.image.load(goodchar_stand_loc)
goodchar_left_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'good_minion_left.png')
goodchar_left_image = pygame.image.load(goodchar_left_loc)
goodchar_right_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'good_minion_right.png')
goodchar_right_image = pygame.image.load(goodchar_right_loc)
evilchar_stand_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'evil_minion_standing.png')
evilchar_stand_image = pygame.image.load(evilchar_stand_loc)
evilchar_left_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'evil_minion_left.png')
evilchar_left_image = pygame.image.load(evilchar_left_loc)
evilchar_right_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'evil_minion_right.png')
evilchar_right_image = pygame.image.load(evilchar_right_loc)

#set food image

#set poison image


#initialize character rectangle 
char_rect = goodchar_stand_image.get_rect()
char_rect.center = (640, 620)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()
    #print(keys)

    #Fill the display
    display_surface.fill(BLACK)

    #Blit the HUD to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(timer_text, timer_rect)

    #Draw platform
    pygame.draw.rect(display_surface, BROWN, (0, 685, WINDOW_WIDTH, 45))

    #Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and char_rect.left > 0:
        char_rect.x -= VELOCITY
        if points > 0:
            display_surface.blit(goodchar_left_image, char_rect)
        else:
            display_surface.blit(evilchar_left_image, char_rect)
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and char_rect.right < WINDOW_WIDTH:
        char_rect.x += VELOCITY
        if points > 0:
            display_surface.blit(goodchar_right_image, char_rect)
        else:
            display_surface.blit(evilchar_right_image, char_rect)
    #if (keys[pygame.K_UP] or keys[pygame.K_w]) and char_rect.top > 0:
    #    char_rect.y -= VELOCITY
    #if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and char_rect.bottom < WINDOW_HEIGHT:
    #    char_rect.y += VELOCITY
    else:
        if points > 0:
            display_surface.blit(goodchar_stand_image, char_rect)
        else:
            display_surface.blit(evilchar_stand_image, char_rect)

    #Check for collision between two rects
    #if char_rect.colliderect(dragon_rect):
    #    print("HIT")
    #    dragon_rect.x = random.randint(0, WINDOW_WIDTH - 80)
    #    dragon_rect.y = random.randint(0, WINDOW_HEIGHT - 80)

    #Fill display surface
    #display_surface.fill((0, 0, 0))

    #Draw rectanges to represent the rects of each object
    #pygame.draw.rect(display_surface, (0, 255, 0), char_rect, 1)
    #pygame.draw.rect(display_surface, (255, 255, 0), dragon_rect, 1)

    #Blit assets
    #display_surface.blit(goodchar_stand_image, char_rect)
    #display_surface.blit(dragon_image, dragon_rect)

    #Update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)
    
#End the game
pygame.quit()
