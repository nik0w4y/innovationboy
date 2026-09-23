import pygame, pytmx, time
playerimg = [pygame.Surface((32,32))] * 12
for i in range(len(playerimg)):
    playerimg[i] = pygame.image.load(f"graphics/player/player{i + 1}.png")
    

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 3
        if keys[pygame.K_a]:
            self.x -= 3
        if keys[pygame.K_s]:
            self.y += 3
        if keys[pygame.K_d]:
            self.x += 3
        return (self.x,self.y)

    def draw(self, time):
        if (time//250)%4 == 0 or (time//250)%4 == 2:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                return playerimg[9]
            if keys[pygame.K_a]:
                return playerimg[3]
            if keys[pygame.K_s]:
                return playerimg[0]
            if keys[pygame.K_d]:
                return playerimg[6]
            else:
                return playerimg[1]
        if (time//250)%4 == 1 or (time//250)%4 == 3:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                return playerimg[11]
            if keys[pygame.K_a]:
                return playerimg[5]
            if keys[pygame.K_s]:
                return playerimg[2]
            if keys[pygame.K_d]:
                return playerimg[8]
            else:
                return playerimg[1]
