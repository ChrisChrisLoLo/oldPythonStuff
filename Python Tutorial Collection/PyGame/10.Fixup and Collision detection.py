import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
#on a scale of 0-255, with 256 elements

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Slither')



clock = pygame.time.Clock()

block_size = 20
FPS = 30

font = pygame.font.SysFont(None,25)


def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0] ,XnY[1] ,block_size,block_size])



def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2 , display_height/2])


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    #We effectively removed the grid lock on the apple
    randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
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

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change



        gameDisplay.fill(white)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY ,AppleThickness,AppleThickness])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList [0]
        snake(block_size, snakeList)


        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        pygame.display.update()


        #IMPLEMPENTING NEW COLLISION CODE SO All SECTIONS OF THE SNAKE HEAD WILL REGISTER WHEN OVER
        #AN APPLE
        #if  (randAppleX+AppleThickness)>=lead_x>=randAppleX and (randAppleY+AppleThickness)>=lead_y>= randAppleY:
            #randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10.0
            #randAppleY = round(random.randrange(0, display_height - AppleThickness))#/10.0)*10.0
            #snakeLength += 1
        if randAppleX <= lead_x <= randAppleX+AppleThickness or randAppleX <= lead_x + block_size <= randAppleX+AppleThickness:
            if randAppleY <= lead_y <= randAppleY+AppleThickness or randAppleY <= lead_y + block_size <= randAppleY+AppleThickness:
                randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - AppleThickness))#/10.0)*10.0
                snakeLength += 1


        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()