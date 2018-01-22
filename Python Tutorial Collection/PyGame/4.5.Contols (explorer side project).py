import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
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
            if event.key == pygame.K_LEFT:
                lead_x_change = -2.5
            if event.key == pygame.K_RIGHT:
                lead_x_change = 2.5

            if event.key == pygame.K_UP:
                lead_y_change = -2.5
            if event.key == pygame.K_DOWN:
                lead_y_change = 2.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(green)
    pygame.draw.rect(gameDisplay, white, [lead_x ,lead_y ,10,10])
    pygame.display.update()

    clock.tick(60)
    #Sets fps, avoid changing it if possible

pygame.quit()
quit()