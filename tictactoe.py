import pygame , sys
pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
#RBG= red, green, blue)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((640, 480))


#Back Ground
background = pygame.image.load("xo.jpg").convert()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')

#pygame.draw.line(screen, RED,(10, 10 ), (300, 300), 10)

def draw_lines():
    #1 horizontal 
    pygame.draw.line(background, RED, (0, 200),(600, 200),LINE_WIDTH )
    #2 horizontal
    pygame.draw.line(background, RED,(0, 400), (600, 400), LINE_WIDTH)
    #1 Vertical
    pygame.draw.line(background, RED,(200, 0),(200, 600), LINE_WIDTH)
    #2 vertical
    pygame.draw.line(background, RED,(400, 0,),(400,600), LINE_WIDTH)
draw_lines()






#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
    pygame.display.update()
    screen.blit(background, (0, 0))
