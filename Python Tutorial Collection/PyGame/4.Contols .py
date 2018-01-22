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
lead_x_change = 0
lead_y_change = 0
clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            #WE USE ELIF TO SAVE PROCESSING POWER, AS IF CHECKS ALL IF STATEMENTS,
            #  WHEREAS ELIF CHECKS THE SUCSESSFUl  IF STATEMENT AND SKIPS THE REST
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0

            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0

            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0

            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

    #We have the bounding line at >= 800 as we are looking at the top left pixel of our square,
    #which can be == 800 past the  visible border
    if lead_x >= 800 or lead_x < 0 or lead_y > 600 or lead_y <0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x ,lead_y ,10,10])
    pygame.display.update()

    clock.tick(15)
    #Sets fps, avoid changing it if possible

pygame.quit()
quit()