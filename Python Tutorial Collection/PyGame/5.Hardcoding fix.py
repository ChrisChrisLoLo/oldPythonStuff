import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
#on a scale of 0-255, with 256 elements

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Slither')

gameExit= False

lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

FPS = 30
block_size = 10

#Creation of variables to enable more effiencient changes in values if they are needed
#They make the code a bit harder to read but a lot more "logical" and easy to edit.
#The general rule of thumb is that if its a number and not 0, it probably should have a variable
while not gameExit:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            #WE USE ELIF TO SAVE PROCESSING POWER, AS IF CHECKS ALL IF STATEMENTS,
            #  WHEREAS ELIF CHECKS THE SUCESSFUl  IF STATEMENT AND SKIPS THE REST
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0

            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0

            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0

            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    #We have the bounding line at >= 800 as we are looking at the top left pixel of our square,
    #which can be == 800 past the  visible border
    if lead_x >= display_width or lead_x < 0 or lead_y > display_height or lead_y <0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x ,lead_y ,block_size,block_size])
    pygame.display.update()

    clock.tick(FPS)
    #Sets fps, avoid changing it if possible

pygame.quit()
quit()