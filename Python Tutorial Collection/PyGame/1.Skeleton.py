import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
#on a scale of 0-255, with 256 elements

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Slither')


gameExit= False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400,300,10,10])
        #where to draw, what color, [posistion width, posistion height, width, height] (draws from top left, with height going downwards)

    gameDisplay.fill(red, rect=[200,200,50,50])
    pygame.display.update()
    # can be more rocessicing efficient option/method, should not be a concern

pygame.quit()
quit()