import pygame , sys
pygame.init()
WIDTH = 600
HEIGHT = 600
#RGB= RED,GREEN,BLUE
#RED = (255, 0, 0)
screen = pygame.display.set_mode((640, 480))


#Back Ground
background = pygame.image.load("xo.jpg").convert()

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
#screen.fill( background )

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
    pygame.display.update()
    screen.blit(background, (0, 0))
