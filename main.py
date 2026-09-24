import pygame, pytmx, time

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
tmxdata = pytmx.load_pygame("data/tmx/overworld.tmx")
mult = 32
start_time = pygame.time.get_ticks()

import player

player1 = player.Player(tmxdata.get_object_by_name("playerspawn").x,tmxdata.get_object_by_name("playerspawn").y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((0,0,0))

    check1 = 1
    i1 = 0
    while check1 == 1:
        if i1 != 1:
            for y in range(tmxdata.layers[i1].height):
                for x in range(tmxdata.layers[i1].width):
                    if tmxdata.layers[i1].data[y][x] != 0:
                        screen.blit(tmxdata.get_tile_image(x, y, i1), (x*mult, y*mult))
        i1 += 1
        if i1 > 3:
            check1 = 0

     
    screen.blit(player1.draw(pygame.time.get_ticks() - start_time), player1.move())
    for y in range(tmxdata.layers[1].height):
        for x in range(tmxdata.layers[1].width):
            if tmxdata.layers[1].data[y][x] != 0:
                screen.blit(tmxdata.get_tile_image(x, y, 1), (x*mult, y*mult))
    pygame.display.flip()


    clock.tick(60)  
pygame.quit()
