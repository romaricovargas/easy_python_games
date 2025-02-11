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
timer = 60
timer_fps = 0

#Set game values
VELOCITY = 7
points = 0

#Set colors
CYAN = (0, 255, 255)
BROWN = (33, 33, 33)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (246, 233, 94 )
ORANGE = (255, 195, 0)
PURPLE = (175, 119, 210)
PURPLE2 = (210, 178, 238)

#Set fonts
font_loc = os.path.join('you_are_what_you_eat', 'fonts', 'SuperDessert-EaAyj.ttf')
font_medium = pygame.font.Font(font_loc, 40)
font_large = pygame.font.Font(font_loc, 50)

#Set Text
score_text = font_medium.render("Score: " + str(points), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font_large.render("You Are What You Eat", True, YELLOW)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

timer_text = font_medium.render("time: " + str(timer), True, ORANGE)
timer_rect = timer_text.get_rect()
timer_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font_medium.render("GAMEOVER", True, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Set sounds and music
food_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'food.wav')
food_sound = pygame.mixer.Sound(food_sound_loc)
food_sound.set_volume(0.3)
poison_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'poison.wav')
poison_sound = pygame.mixer.Sound(poison_sound_loc)
poison_sound.set_volume(0.1)
turn_good_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'turn_good.wav')
turn_good_sound = pygame.mixer.Sound(turn_good_sound_loc)
turn_good_sound.set_volume(0.4)
turn_evil_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'turn_evil.wav')
turn_evil_sound = pygame.mixer.Sound(turn_evil_sound_loc)
turn_evil_sound.set_volume(0.2)

music_loc = os.path.join('you_are_what_you_eat', 'sounds', 'kid-games-music-comedy-situation.mp3')
pygame.mixer.music.load(music_loc)

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
food_image_list = []
food_folder = os.path.join('you_are_what_you_eat', 'images', 'food')
for f in os.listdir(food_folder):
    f_loc = os.path.join(food_folder, f)
    food_image_list.append(pygame.image.load(f_loc))

#set poison image
poison_image_list = []
poison_folder = os.path.join('you_are_what_you_eat', 'images', 'poison')
for p in os.listdir(poison_folder):
    p_loc = os.path.join(poison_folder, p)
    poison_image_list.append(pygame.image.load(p_loc))

#initialize character rectangle 
char_rect = goodchar_stand_image.get_rect()
char_rect.center = (640, 620)

#Food and poison rendering flags
food_01_rendered = False
food_02_rendered = False
food_03_rendered = False
food_04_rendered = False
food_05_rendered = False
poison_01_rendered = False
poison_02_rendered = False
poison_03_rendered = False
poison_04_rendered = False

#The main game loop
pygame.mixer.music.play(-1, 0.0)
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

    #Blit texts to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(timer_text, timer_rect)

    #Draw food
    if not food_01_rendered:
        food_01_image = random.choice(food_image_list)
        food_01_image = pygame.transform.scale(food_01_image, (80, 80))
        food_01_rect = food_01_image.get_rect()
        food_01_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        food_01_speed = random.randint(2, 8)
        food_01_rendered = True
    food_01_rect.y += food_01_speed
    display_surface.blit(food_01_image, food_01_rect)

    if not food_02_rendered:
        food_02_image = random.choice(food_image_list)
        food_02_image = pygame.transform.scale(food_02_image, (80, 80))
        food_02_rect = food_02_image.get_rect()
        food_02_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        food_02_speed = random.randint(2, 8)
        food_02_rendered = True
    food_02_rect.y += food_02_speed
    display_surface.blit(food_02_image, food_02_rect)

    if not food_03_rendered:
        food_03_image = random.choice(food_image_list)
        food_03_image = pygame.transform.scale(food_03_image, (80, 80))
        food_03_rect = food_03_image.get_rect()
        food_03_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        food_03_speed = random.randint(2, 8)
        food_03_rendered = True
    food_03_rect.y += food_03_speed
    display_surface.blit(food_03_image, food_03_rect)

    if not food_04_rendered:
        food_04_image = random.choice(food_image_list)
        food_04_image = pygame.transform.scale(food_04_image, (80, 80))
        food_04_rect = food_04_image.get_rect()
        food_04_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        food_04_speed = random.randint(2, 8)
        food_04_rendered = True
    food_04_rect.y += food_04_speed
    display_surface.blit(food_04_image, food_04_rect)

    if not food_05_rendered:
        food_05_image = random.choice(food_image_list)
        food_05_image = pygame.transform.scale(food_05_image, (80, 80))
        food_05_rect = food_05_image.get_rect()
        food_05_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        food_05_speed = random.randint(2, 8)
        food_05_rendered = True
    food_05_rect.y += food_05_speed
    display_surface.blit(food_05_image, food_05_rect)

    if not poison_01_rendered:
        poison_01_image = random.choice(poison_image_list)
        poison_01_image = pygame.transform.scale(poison_01_image, (80, 80))
        poison_01_rect = poison_01_image.get_rect()
        poison_01_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        poison_01_speed_y = random.randint(5, 9)
        poison_01_speed_x = random.choice([-1, 1])
        poison_01_rendered = True
    poison_01_rect.y += poison_01_speed_y
    poison_01_rect.x += poison_01_speed_x
    display_surface.blit(poison_01_image, poison_01_rect)

    if not poison_02_rendered:
        poison_02_image = random.choice(poison_image_list)
        poison_02_image = pygame.transform.scale(poison_02_image, (80, 80))
        poison_02_rect = poison_02_image.get_rect()
        poison_02_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        poison_02_speed_y = random.randint(5, 9)
        poison_02_speed_x = random.choice([-1, 1])
        poison_02_rendered = True
    poison_02_rect.y += poison_02_speed_y
    poison_02_rect.x += poison_02_speed_x
    display_surface.blit(poison_02_image, poison_02_rect)

    if not poison_03_rendered:
        poison_03_image = random.choice(poison_image_list)
        poison_03_image = pygame.transform.scale(poison_03_image, (80, 80))
        poison_03_rect = poison_03_image.get_rect()
        poison_03_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        poison_03_speed_y = random.randint(5, 9)
        poison_03_speed_x = random.choice([-1, 1])
        poison_03_rendered = True
    poison_03_rect.y += poison_03_speed_y
    poison_03_rect.x += poison_03_speed_x
    display_surface.blit(poison_03_image, poison_03_rect)

    if not poison_04_rendered:
        poison_04_image = random.choice(poison_image_list)
        poison_04_image = pygame.transform.scale(poison_04_image, (80, 80))
        poison_04_rect = poison_04_image.get_rect()
        poison_04_rect.center = (random.randint(100, WINDOW_WIDTH-100), 110)
        poison_04_speed_y = random.randint(5, 9)
        poison_04_speed_x = random.choice([-1, 1])
        poison_04_rendered = True
    poison_04_rect.y += poison_04_speed_y
    poison_04_rect.x += poison_04_speed_x
    display_surface.blit(poison_04_image, poison_04_rect)

    #Draw platform
    platform_rect = pygame.draw.rect(display_surface, BROWN, (0, 685, WINDOW_WIDTH, 45))

    #Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and char_rect.left > 0:
        char_rect.x -= VELOCITY
        if points >= 0:
            display_surface.blit(goodchar_left_image, char_rect)
        else:
            display_surface.blit(evilchar_left_image, char_rect)
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and char_rect.right < WINDOW_WIDTH:
        char_rect.x += VELOCITY
        if points >= 0:
            display_surface.blit(goodchar_right_image, char_rect)
        else:
            display_surface.blit(evilchar_right_image, char_rect)
    else:
        if points >= 0:
            display_surface.blit(goodchar_stand_image, char_rect)
        else:
            display_surface.blit(evilchar_stand_image, char_rect)

    #Check for collision between two rects
    prev_points = points
    if char_rect.colliderect(food_01_rect):
        food_01_rendered = False
        points += 1
        food_sound.play()
    if char_rect.colliderect(food_02_rect):
        food_02_rendered = False
        points += 1
        food_sound.play()
    if char_rect.colliderect(food_03_rect):
        food_03_rendered = False
        points += 1
        food_sound.play()
    if char_rect.colliderect(food_04_rect):
        food_04_rendered = False
        points += 1
        food_sound.play()
    if char_rect.colliderect(food_05_rect):
        food_05_rendered = False
        points += 1
        food_sound.play()
    if food_01_rect.colliderect(platform_rect):
        food_01_rendered = False
    if food_02_rect.colliderect(platform_rect):
        food_02_rendered = False
    if food_03_rect.colliderect(platform_rect):
        food_03_rendered = False
    if food_04_rect.colliderect(platform_rect):
        food_04_rendered = False
    if food_05_rect.colliderect(platform_rect):
        food_05_rendered = False
    if char_rect.colliderect(poison_01_rect):
        poison_01_rendered = False
        points -= 1
        poison_sound.play()
    if char_rect.colliderect(poison_02_rect):
        poison_02_rendered = False
        points -= 1
        poison_sound.play()
    if char_rect.colliderect(poison_03_rect):
        poison_03_rendered = False
        points -= 1
        poison_sound.play()
    if char_rect.colliderect(poison_04_rect):
        poison_04_rendered = False
        points -= 1
        poison_sound.play()
    if poison_01_rect.colliderect(platform_rect) or poison_01_rect.y > WINDOW_HEIGHT:
        poison_01_rendered = False
    if poison_02_rect.colliderect(platform_rect) or poison_02_rect.y > WINDOW_HEIGHT:
        poison_02_rendered = False
    if poison_03_rect.colliderect(platform_rect) or poison_03_rect.y > WINDOW_HEIGHT:
        poison_03_rendered = False
    if poison_04_rect.colliderect(platform_rect) or poison_04_rect.y > WINDOW_HEIGHT:
        poison_04_rendered = False

    if prev_points == 0 and points == -1:
        turn_evil_sound.play()
    if prev_points == -1 and points == 0:
        turn_good_sound.play()


    #Change text color
    if points >= 0:
        score_text = font_medium.render("Score: " + str(points), True, ORANGE)
        title_text = font_large.render("You Are What You Eat", True, YELLOW)
        timer_text = font_medium.render("time: " + str(timer), True, ORANGE)
    else:
        score_text = font_medium.render("Score: " + str(points), True, PURPLE)
        title_text = font_large.render("You Are What You Eat", True, PURPLE2)
        timer_text = font_medium.render("time: " + str(timer), True, PURPLE)

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

    #Compute time
    if timer_fps >= FPS:
        timer -= 1
        timer_fps = 0
    else:
        timer_fps += 1

    #Tick the clock
    clock.tick(FPS)
    
#End the game
pygame.quit()
