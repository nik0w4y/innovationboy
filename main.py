from typing import dataclass_transform

import pygame, pytmx

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
tmxdata = pytmx.load_pygame("data/tmx/overworld.tmx")
player = pygame.image.load("graphics/player/player1.png")
mult = 32
print(tmxdata.layers,"\n")
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    check1 = 1
    i1 = 0
    while check1 == 1:
        for y in range(tmxdata.layers[i1].height):
            for x in range(tmxdata.layers[i1].width):
                if tmxdata.layers[i1].data[y][x] != 0:
                    screen.blit(tmxdata.get_tile_image(x, y, i1), (x*mult, y*mult))
        i1 += 1
        if i1 > 3:
            check1 = 0


     
    screen.blit(player, (tmxdata.get_object_by_name("playerspawn").x, tmxdata.get_object_by_name("playerspawn").y))
    pygame.display.flip()


    clock.tick(60)  

pygame.quit()
