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

block_size = 10
FPS = 30

font = pygame.font.SysFont(None,25)

def snake(lead_x,lead_y,block_size): #snake function. Used to remove bulk of code from gameLoop, need

    pygame.draw.rect(gameDisplay, green, [lead_x ,lead_y ,block_size,block_size])
def message_to_screen(msg,color): #message function, renders a font and then displays it
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2 , display_height/2])


def gameLoop():     #Moved changing variables and all of the logic into a gameLoop function. The logic and
                    #changing variables must be in the same scope.
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    #apple coodinates, with the block size preventing the apple to be drawn out of the screen
    #we use the round function to allign the apples to coodinates in multiples of 10. We do this by
    #getting the raw rand # and dividing it by 10, only to round it and multiply it again to lock it into a multiple
    randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
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

        if lead_x >= display_width or lead_x < 0 or lead_y > display_height or lead_y <0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change



        gameDisplay.fill(white)
        #Drawing for apple. Like a painting, we want to draw items in the background first, and the foreground last
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY ,block_size,block_size])
        snake(lead_x, lead_y, block_size)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            #Apple collision and regeneration
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()