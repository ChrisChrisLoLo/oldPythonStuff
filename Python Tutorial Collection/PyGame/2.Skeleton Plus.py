import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
#on a scale of 0-255, with 256 elements

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Slither')

gameExit= False

lead_x = 300
lead_y = 300

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400,300,10,10])
        #where to draw, what color, [posistion width, posistion height, width, height] (draws from top left, with height going downwards)

    gameDisplay.fill(red, rect=[200,200,50,50])
    pygame.display.update()
    # can be more rocessicing efficient option/method, should not be a concern

pygame.quit()
quit()