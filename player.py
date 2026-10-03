import pygame, pytmx, time

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.playerimg = [pygame.Surface((32,32))] * 12
        for i in range(len(self.playerimg)):
            self.playerimg[i] = pygame.image.load(f"graphics/player/player{i + 1}.png")
            
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
                return self.playerimg[9]
            if keys[pygame.K_a]:
                return self.playerimg[3]
            if keys[pygame.K_s]:
                return self.playerimg[0]
            if keys[pygame.K_d]:
                return self.playerimg[6]
            else:
                return self.playerimg[1]
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                return self.playerimg[11]
            if keys[pygame.K_a]:
                return self.playerimg[5]
            if keys[pygame.K_s]:
                return self.playerimg[2]
            if keys[pygame.K_d]:
                return self.playerimg[8]
            else:
                return self.playerimg[1]
