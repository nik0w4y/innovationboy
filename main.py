import pygame, pytmx, time
import player

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
tmxdata = pytmx.load_pygame("data/tmx/overworld.tmx")
mult = 32
start_time = pygame.time.get_ticks()
player1 = player.Player(tmxdata.get_object_by_name("playerspawn").x,tmxdata.get_object_by_name("playerspawn").y)
middlex = screen.width/2 - 32
middley = screen.height/2 - 32

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((0,0,0))
    
    player1.move()  
    if tmxdata.layers[0].data[int(player1.y/mult)][int(player1.x/mult)] != 0 and tmxdata.layers[0].data[int(player1.y/mult)][int(player1.x/mult) + 1] != 0:
        prevplayerx = player1.x
        prevplayery = player1.y
    else:
        player1.x = prevplayerx
        player1.y = prevplayery


    for i in range(4):
        if i == 2:
            continue
        for y in range(tmxdata.layers[i].height):
            for x in range(tmxdata.layers[i].width):
                if tmxdata.layers[i].data[y][x] != 0:
                    screen.blit(tmxdata.get_tile_image(x, y, i), (x*mult + middlex - player1.x, y*mult + middley - player1.y + 16))

    screen.blit(player1.draw(pygame.time.get_ticks() - start_time), ((middlex, middley)))

    for y in range(tmxdata.layers[2].height):
        for x in range(tmxdata.layers[2].width):
            if tmxdata.layers[2].data[y][x] != 0:
                screen.blit(tmxdata.get_tile_image(x, y, 2), (x*mult + middlex - player1.x, y*mult + middley - player1.y + 16))
    pygame.display.flip()


    clock.tick(30)  
pygame.quit()
