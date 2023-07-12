import pygame
NERO=(0,0,0)
class Tavolo(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

       pygame.sprite.Sprite.__init__(self)
       super().__init__()

       self.image = pygame.Surface([width, height])
       self.image.fill(NERO)
       self.image.set_colorkey(NERO)
       pygame.draw.rect(self.image,color,[0,0,width,height])

       self.rect = self.image.get_rect()

    def muoviSU(self,pixel):
        self.rect.y=self.rect.y-pixel
        if self.rect.y<0:
            self.rect.y=0

    def muoviGIU(self,pixel):
        self.rect.y=self.rect.y+pixel
        if self.rect.y>500:
            self.rect.y=500

