import pygame
import time
from lib import *
class Warrior(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #size
        self.image = pygame.image.load(os.path.join(img_folder,"mon_left_walk_1.png")).convert()
        self.image.set_colorkey(warriorBg)
        self.rect = self.image.get_rect()
        #color


        #location of this class
        self.rect.center = (800,50)
        self.speedX = 0
        self.speedY = 0

        #check wall


    def update(self):
        self.speedX = 0
        self.speedY = 0
        self.shootCount = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.speedX = -vel


        if keys[pygame.K_RIGHT] and self.rect.right < display_width:
            self.speedX = +vel

        if keys[pygame.K_UP] and self.rect.top > 0:
            self.speedY = -vel
        if keys[pygame.K_DOWN] and self.rect.bottom < display_height:
            self.speedY = +vel
        if keys[pygame.K_p]:
            self.shoot()

        self.rect.x += self.speedX
        self.rect.y += self.speedY
    def killSelf(self):
        self.kill()

    def shoot(self):
        bullet = BulletLeft(self.rect.left, self.rect.centery)
        all_sprites_list.add(bullet)
        bulletsLeft.add(bullet)




    def walkImage(self):
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = []
        self.walkLeft = []

        self.walkRight.append( pygame.image.load(os.path.join(img_folder,"cat_right_walk_1.png")).convert() )
        self.walkRight.append( pygame.image.load(os.path.join(img_folder,"cat_right_walk_2.png")).convert() )
        self.walkRight.append( pygame.image.load(os.path.join(img_folder,"cat_right_walk_3.png")).convert() )
        self.walkRight.append( pygame.image.load(os.path.join(img_folder,"cat_right_walk_4.png")).convert() )
        self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"cat_left_walk_1.png")).convert() )
        self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"cat_left_walk_2.png")).convert() )
        self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"cat_left_walk_3.png")).convert() )
        self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"cat_left_walk_4.png")).convert() )

        print("self.left: {}".format(self.walkLeft) )
        print("self.right: {}".format(self.walkRight) )
        if self.walkCount +1 >= 36:
            self.walkCount = 0
        if self.left:
            print(walkCount)
            self.image = self.walkLeft[self.walkCount%4]
            self.walkCount += 1


        elif self.right:
            self.image = self.walkRight[self.walkCount%4]
            self.walkCount += 1
        else:
            self.image = pygame.image.load(os.path.join(img_folder,"cat_left_walk_1.png")).convert()
        self.image.set_colorkey(warriorBg)
        #get rectangle position
        self.rect = self.image.get_rect()



class Goblin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #size

        self.image = pygame.image.load(os.path.join(img_folder,"cat_walk.gif")).convert()
        #color
        self.image.set_colorkey(goblinBg)
        self.rect = self.image.get_rect()

        #location of this class
        self.rect.center = (100,300)
        self.speedX = 0
        self.speedY = 0


    def update(self):
        self.speedX = 0
        self.speedY = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.speedX = -vel
        if keys[pygame.K_d] and self.rect.right < display_width:
            self.speedX = +vel
        if keys[pygame.K_w] and self.rect.top > 0:
            self.speedY = -vel
        if keys[pygame.K_s] and self.rect.bottom < display_height:
            self.speedY = +vel
        if keys[pygame.K_LCTRL]:
            self.shoot()
        self.rect.x += self.speedX
        self.rect.y += self.speedY
    def killSelf(self):
        self.kill()

    # def walkImage(self):
    #     self.left = False
    #     self.right = False
    #     self.walkCount = 0
    #     self.walkRight = []
    #     self.walkLeft = []
    #     self.walkRight.append( pygame.image.load(os.path.join(img_folder,"mon_right_walk_1.png")).convert() )
    #     self.walkRight.append( pygame.image.load(os.path.join(img_folder,"mon_right_walk_2.png")).convert() )
    #     self.walkRight.append( pygame.image.load(os.path.join(img_folder,"mon_right_walk_3.png")).convert() )
    #     self.walkRight.append( pygame.image.load(os.path.join(img_folder,"mon_right_walk_4.png")).convert() )
    #     self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"mon_left_walk_1.png")).convert() )
    #     self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"mon_left_walk_2.png")).convert() )
    #     self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"mon_left_walk_3.png")).convert() )
        # self.walkLeft.append( pygame.image.load(os.path.join(img_folder,"mon_left_walk_4.png")).convert() )
        # self.walkRight=[pygame.image.load(os.path.join(img_folder,"mon_right_walk_1.png")),pygame.image.load(os.path.join(img_folder,"mon_right_walk_2.png")),pygame.image.load(os.path.join(img_folder,"mon_right_walk_3.png")),pygame.image.load(os.path.join(img_folder,"mon_right_walk_4.png"))]
        # self.walkLeft=[pygame.image.load(os.path.join(img_folder,"mon_left_walk_1.png")),pygame.image.load(os.path.join(img_folder,"mon_left_walk_2.png")),pygame.image.load(os.path.join(img_folder,"mon_left_walk_3.png")),pygame.image.load(os.path.join(img_folder,"mon_left_walk_4.png"))]

    def shoot(self):
        bullet = BulletRight(self.rect.right, self.rect.centery)
        all_sprites_list.add(bullet)
        bulletsRight.add(bullet)


class BulletLeft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -10

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()

class BulletRight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = +10


    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > display_width:
            self.kill()
