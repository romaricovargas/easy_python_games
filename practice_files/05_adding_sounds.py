import pygame
import os

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds!")

#Sound locations
music_loc = os.path.join('practice_files', '05_sounds', 'music.wav')
sound_effect_01_loc = os.path.join('practice_files', '05_sounds', 'sound_effect_01.wav')
sound_effect_02_loc = os.path.join('practice_files', '05_sounds', 'sound_effect_02.wav')

#Load sounds
sound_effect_01 = pygame.mixer.Sound(sound_effect_01_loc)
sound_effect_02 = pygame.mixer.Sound(sound_effect_02_loc)

#Play sound effects
sound_effect_01.play()
pygame.time.delay(2000)   #2000 milliseconds
sound_effect_02.play()
pygame.time.delay(2000)   #2000 milliseconds

#Change the volume of a sound effect
sound_effect_02.set_volume(.1)
sound_effect_02.play()
pygame.time.delay(2000)   #2000 milliseconds

#Load background music
pygame.mixer.music.load(music_loc)

#Play and stop the music
pygame.mixer.music.play(-1, 0.0)   # -1 means loop forever, 0.0 is the starting time
pygame.time.delay(5000)
pygame.mixer.music.stop()

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#End the game
pygame.quit()
