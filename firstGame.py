import pygame
import sys,os
pygame.init()

winWidth = 500
winHeight = 480
win = pygame.display.set_mode((winWidth,winHeight))
path = 'C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\'
pygame.display.set_caption("First game!")


bg = pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\bg.jpg')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = [pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R1.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R2.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R3.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R4.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R5.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R6.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R7.png')
        ,pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R8.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\R9.png')]
        self.walkLeft = [pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L1.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L2.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L3.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L4.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L5.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L6.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L7.png')
        ,pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L8.png'),pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\L9.png')]
        self.char = pygame.image.load('C:\\Users\\user\\Desktop\\Programming\\python\\pygame\\practice\\pygame_tutorial\\standing.png')


    def draw(self,win):
        pygame.draw.rect(win,(23,180,102),(self.x,self.y,self.width,self.height))
        win.blit(bg, (0,0))
        if self.walkCount +1 >=27:
            self.walkCount= 0
        if self.left:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.char, (self.x,self.y))

        pygame.display.update()

#mainloop
run = True
player1 = Player(40,400,50,50)
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player1.x > player1.vel:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
    elif keys[pygame.K_RIGHT] and player1.x < winWidth - player1.width - player1.vel:
        player1.x += player1.vel
        player1.left = False
        player1.right = True
    else:
        player1.right=False
        player1.left=False
        player1.walkCount = 0
    if not(player1.isJump):
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < winHeight - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            player1.isJump = True
    else:
        if player1.jumpCount >= -10:
            neg = 1
            if (player1.jumpCount <= 0):
                neg = -1
            player1.y -= (player1.jumpCount **2) *0.4 * neg
            # x += (jumpCount **2) *0.3
            player1.jumpCount -= 1


        else:
            player1.isJump = False
            player1.jumpCount = 10

    player1.draw(win)

pygame.quit()
