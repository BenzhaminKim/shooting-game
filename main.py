import pygame,sys,os
from lib import *
from character import *
pygame.init()



#set Variables

#add Sprite
player1 = Warrior()
player2 = Goblin()
all_sprites_list.add(player1)
all_sprites_list.add(player2)
#start gamew

while running:
    clock.tick(36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #game Logic
    all_sprites_list.update()

    #collide
    pygame.sprite.groupcollide(bulletsLeft,bulletsRight,True,True)
    catWin = pygame.sprite.spritecollide(player1,bulletsRight,True)

    monWin = pygame.sprite.spritecollide(player2,bulletsLeft,True)
    if catWin:
        print("Cat win!")
        player1.killSelf()
    if monWin:
        print("Mon win!")
        player2.killSelf()
    #draw
    display.blit(bg, (0,0))
    all_sprites_list.draw(display)
    pygame.display.flip()
pygame.quit()
