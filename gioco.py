import pygame
from palla import Palla
from tavolo import Tavolo
from random import randint


pygame.init()

NERO=(0,0,0)
BIANCO=(255,255,255)

grandezza=(800,600)
schermo=pygame.display.set_mode(grandezza)
pygame.display.set_caption("Barda pong")

tavolo1=Tavolo(BIANCO,10,100)
tavolo1.rect.x=30
tavolo1.rect.y=250

tavolo2=Tavolo(BIANCO,10,100)
tavolo2.rect.x=770
tavolo2.rect.y=250

palla=Palla(BIANCO,10,10)
palla.rect.x=400
palla.rect.y=295

listasprite=pygame.sprite.Group()

listasprite.add(tavolo1)
listasprite.add(tavolo2)
listasprite.add(palla)

loop= True #continua all'infinito

clock= pygame.time.Clock()

punteggio1=0
punteggio2=0

lock1=False
lock2=False

timer=1


while loop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            loop= False

    tasti=pygame.key.get_pressed()
    if tasti[pygame.K_w] and lock1==False:
        tavolo1.muoviSU(5)

    if tasti[pygame.K_s] and lock1==False:
        tavolo1.muoviGIU(5)

    if tasti[pygame.K_UP] and lock2==False:
        tavolo2.muoviSU(5)

    if tasti[pygame.K_DOWN] and lock2==False:
        tavolo2.muoviGIU(5)

    listasprite.update()

    if palla.rect.x>=790:
        punteggio1=punteggio1+1
        palla.velocity[0]=-palla.velocity[0]
    if palla.rect.x<=0:
        punteggio2=punteggio2+1
        palla.velocity[0]=-palla.velocity[0]

    if palla.rect.y > 590:
        palla.velocity[1] = -palla.velocity[1]
    if palla.rect.y <= 0:
        palla.velocity[1] = -palla.velocity[1]

    if pygame.sprite.collide_mask(palla,tavolo1) or pygame.sprite.collide_mask(palla,tavolo2):
        palla.rimbalza()

    schermo.fill(NERO)
    pygame.draw.line(schermo,BIANCO,[399,0],[399,600],3)
    listasprite.draw(schermo)

    font=pygame.font.Font(None,74)
    text=font.render(str(punteggio1),1,BIANCO)

    schermo.blit(text,(300,10))
    text=font.render(str(punteggio2),1,BIANCO)

    schermo.blit(text,(500,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()