import os,sys,pygame

WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
warriorBg = (0,114,188)
goblinBg = (0,114,188)
#set Variables
display_width = 852
display_height = 480

#speed of the character
vel = 5

#set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
bg = pygame.image.load(os.path.join(img_folder,"bg.jpg"))

display = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
all_sprites_list = pygame.sprite.Group()
bulletsRight = pygame.sprite.Group()
bulletsLeft = pygame.sprite.Group()
running = True
