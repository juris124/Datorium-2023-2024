import pygame
import random

pygame.init() # inicializējam pygame

platums = 500
augstums = 600

# definēsim logu ar izmēru px
window = pygame.display.set_mode([platums, augstums])

KOSMOSAKUGIS = pygame.image.load('Pygames/kosmosaKugis.png')
FONS = pygame.image.load('Pygames/foons.jpg')
RAKETE = pygame.image.load('Pygame/rakete.jpg')

kosmosakugis_x = 100
kosmosakugis_y = 100
spaceship_left_change = 0
spaceship_top_change = 0

solis = 0.3

rakete_koord =[]

while True:
    notikumi = pygame.event.get()
    for notikums  in notikumi:
        if notikums.type == pygame.QUIT:
            pygame.quit()
        print(notikums)        
        if notikums.type == pygame.KEYDOWN:
            if notikums.key == pygame.K_t:
                kosmosakugis_x = random.randint(75, platums-150)
                kosmosakugis_y = random.randint(75, augstums-150)
            
            if notikums.key == pygame.K_LEFT:
                spaceship_left_change = -solis
                spaceship_top_change = 0

            if notikums.key == pygame.K_RIGHT:
                spaceship_left_change = solis
                spaceship_top_change = 0
            
            if notikums.key == pygame.K_DOWN:
                spaceship_left_change = 0
                spaceship_top_change = solis

            if notikums.key == pygame.K_UP:
                spaceship_left_change = 0
                spaceship_top_change = -solis
            
            if notikums.key == pygame.K_s:
                spaceship_left_change = 0
                spaceship_top_change = 0

            if notikums.key == pygame.K_SPACE:
                rakete_x = kosmosakugis_x + (RAKETE.get_width()/2)
                rakete_y = kosmosakugis_y + (RAKETE.get_height())

                rakete_koord.append([rakete_x, rakete_y])

    if kosmosakugis_x <= 0 or kosmosakugis_x > platums - 110:
        spaceship_left_change = -spaceship_left_change
    
    if kosmosakugis_y <= 0 or kosmosakugis_y > augstums - 100:
        spaceship_top_change = -spaceship_top_change

    kosmosakugis_x += spaceship_left_change
    kosmosakugis_y += spaceship_top_change

    
    #window.fill([255,222,34])    
    window.blit(FONS,[0,0])
    window.blit(KOSMOSAKUGIS,[kosmosakugis_x,kosmosakugis_y])
    window.blit(RAKETE,[kosmosakugis_x,kosmosakugis_y])
    pygame.display.update()
