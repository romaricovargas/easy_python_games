import asyncio
import pygame
import os
import random

async def main():

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
    points = 0
    high_score = 0
    intro_run_speed = 6
    timer = 60
    frame_counter = 0

    #Set game flags
    game_over = False
    not_continue = False
    intro = True

    #Set colors
    GRAY = (33, 33, 33)
    BLACK = (0, 0, 0)
    YELLOW = (246, 233, 94 )
    ORANGE = (255, 195, 0)
    PURPLE = (175, 119, 210)
    PURPLE2 = (210, 178, 238)

    #Set fonts
    font_loc = os.path.join('you_are_what_you_eat', 'fonts', 'SuperDessert-EaAyj.ttf')
    font_medium = pygame.font.Font(font_loc, 40)
    font_large = pygame.font.Font(font_loc, 50)
    font_extra_large = pygame.font.Font(font_loc, 70)

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

    main_title_text = font_extra_large.render("YOU ARE WHAT YOU EAT!", True, YELLOW)
    main_title_rect = main_title_text.get_rect()
    main_title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 20)

    good_instruction_text = font_medium.render("Savor the fruits", True, ORANGE)
    good_instruction_rect = good_instruction_text.get_rect()
    good_instruction_rect.center = (WINDOW_WIDTH//2 - 210, WINDOW_HEIGHT//2 + 50)

    bad_instruction_text = font_medium.render("Skip the bad bites", True, PURPLE2)
    bad_instruction_rect = bad_instruction_text.get_rect()
    bad_instruction_rect.center = (WINDOW_WIDTH//2 + 210, WINDOW_HEIGHT//2 + 50)

    play_game_text = font_medium.render("press any key to play", True, PURPLE)
    play_game_rect = play_game_text.get_rect()
    play_game_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 180)

    game_over_text = font_large.render("Time's up!", True, YELLOW)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 30)

    last_score_text = font_medium.render("your score is 00", True, ORANGE)
    last_score_rect = last_score_text.get_rect()
    last_score_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 30)

    high_score_text = font_medium.render("high score is 00", True, PURPLE)
    high_score_rect = high_score_text.get_rect()
    high_score_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)

    continue_text = font_medium.render("press any key to continue", True, PURPLE2)
    continue_rect = continue_text.get_rect()
    continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 130)

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
    game_over_sound_loc = os.path.join('you_are_what_you_eat', 'sounds', 'game_over.wav')
    game_over_sound = pygame.mixer.Sound(game_over_sound_loc)

    music_loc = os.path.join('you_are_what_you_eat', 'sounds', 'kid-games-music-comedy-situation.wav')
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
    minion_banana_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'minion_banana.png')
    minion_banana_image = pygame.image.load(minion_banana_loc)
    minion_fruits_loc = os.path.join('you_are_what_you_eat', 'images', 'characters', 'minion_fruits.png')
    minion_fruits_image = pygame.image.load(minion_fruits_loc)
    minion_fruits_image = pygame.transform.scale(minion_fruits_image, (220, 220))

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

    #food and poison rendering flags
    food_01_rendered = False
    food_02_rendered = False
    food_03_rendered = False
    food_04_rendered = False
    food_05_rendered = False
    poison_01_rendered = False
    poison_02_rendered = False
    poison_03_rendered = False
    poison_04_rendered = False
    minion_fruits_rendered = False

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

        #INTRO
        while intro:
            display_surface.fill(BLACK)
            display_surface.blit(main_title_text, main_title_rect)
            display_surface.blit(good_instruction_text, good_instruction_rect)

            if not minion_fruits_rendered:
                minion_fruits_rect = minion_fruits_image.get_rect()
                minion_fruits_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 180)
                minion_fruits_rendered = True
            if minion_fruits_rect.x >= (WINDOW_WIDTH - 300) or minion_fruits_rect.x <= 100:
                intro_run_speed = -1 * intro_run_speed    
            minion_fruits_rect.x += intro_run_speed
            display_surface.blit(minion_fruits_image, minion_fruits_rect)

            display_surface.blit(bad_instruction_text, bad_instruction_rect)
            display_surface.blit(play_game_text, play_game_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    intro = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(-1, 0.0)
                if event.type == pygame.QUIT:
                    intro = False
                    not_continue = True
            clock.tick(FPS)
            

        #GAME OVER
        if timer <= 0:
            game_over = True
            if points > high_score:
                high_score = points
            minion_banana_rec = minion_banana_image.get_rect()
            minion_banana_rec.center = (WINDOW_WIDTH/2, 220)
            display_surface.blit(minion_banana_image, minion_banana_rec)
            display_surface.blit(game_over_text, game_over_rect)
            last_score_text = font_medium.render("your score is " + str(points), True, ORANGE)
            display_surface.blit(last_score_text, last_score_rect)
            high_score_text = font_medium.render("high score is " + str(high_score), True, PURPLE2)
            display_surface.blit(high_score_text, high_score_rect)
            pygame.display.update()
            pygame.mixer.music.stop()
            game_over_sound.play()
            pygame.time.delay(2000)
            pygame.event.get()
            display_surface.blit(continue_text, continue_rect)
            pygame.display.update()

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_over_sound.stop()
                    food_01_rendered = False
                    food_02_rendered = False
                    food_03_rendered = False
                    food_04_rendered = False
                    food_05_rendered = False
                    poison_01_rendered = False
                    poison_02_rendered = False
                    poison_03_rendered = False
                    poison_04_rendered = False
                    points = 0
                    timer = 60
                    char_rect.center = (640, 620)
                    pygame.mixer.music.play(-1, 0.0)
                    display_surface.fill(BLACK)
                    game_over = False
                if event.type == pygame.QUIT:
                    game_over = False
                    not_continue = True

        if not_continue:
            break

        #GAME PROPER
        
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
        platform_rect = pygame.draw.rect(display_surface, GRAY, (0, 685, WINDOW_WIDTH, 45))

        #Move the character continuously
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


        #Change text color based on points
        if points >= 0:
            score_text = font_medium.render("Score: " + str(points), True, ORANGE)
            title_text = font_large.render("You Are What You Eat", True, YELLOW)
            timer_text = font_medium.render("time: " + str(timer), True, ORANGE)
        else:
            score_text = font_medium.render("Score: " + str(points), True, PURPLE)
            title_text = font_large.render("You Are What You Eat", True, PURPLE2)
            timer_text = font_medium.render("time: " + str(timer), True, PURPLE)

        #Update display
        pygame.display.update()

        #Compute time
        if frame_counter >= FPS:
            timer -= 1
            frame_counter = 0
        else:
            frame_counter += 1

        #Tick the clock
        clock.tick(FPS)
        
    #End the game
    pygame.quit()

    await asyncio.sleep(0)

asyncio.run(main())