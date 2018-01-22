import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
deepRed = (136,0,21)
#on a scale of 0-255, with 256 elements

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Slither")

#A custom icon is set up, the apple sprite is used.
#The best icon resolution is 32 x 32
icon = pygame.image.load("Apple.png")
pygame.display.set_icon(icon)

#You can also give the complete path to your image if it is not in the same directory
#Be sure to use forwards slashes instead of backslash
# ex. ("C:desktop\route\file")

snakeHeadImg = pygame.image.load("SnakeHead.png")
appleImg = pygame.image.load("Apple.png")

clock = pygame.time.Clock()
AppleThickness = 30
block_size = 20

FPS = 15

direction = "right"

#To upload a font from a custom directory and not system font, put in pygame.font.Font([pathname])
smallFont = pygame.font.SysFont("centurygothic",25)
mediumFont = pygame.font.SysFont("centurygothic",50)
largeFont = pygame.font.SysFont("centurygothic",80)

#Introduced Intro module. Pretty straight forward
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither", green, -100, largeFont)
        message_to_screen("Eat as many red apples as you can", black, -30)
        message_to_screen("The more you eat, the longer you get", black, 10)
        message_to_screen("If you run into yourself, or the edges, you lose!", black, 50)
        message_to_screen("Press C to play or Q to quit", black, 120)
        pygame.display.update()
        #For static menus, 15 fps isnt nessicary, and is actually pretty high
        clock.tick(15)

def snake(block_size, snakeList):

    #logic r=thgat rotates head img. angles rotates clockwise.
    if direction =="right":
        headImg = pygame.transform.rotate(snakeHeadImg,270)
    if direction =="left":
        headImg = pygame.transform.rotate(snakeHeadImg,90)
    if direction =="up":
        headImg = pygame.transform.rotate(snakeHeadImg,0)
    if direction =="down":
        headImg = pygame.transform.rotate(snakeHeadImg,180)

    gameDisplay.blit(headImg, (snakeList[-1][0], snakeList[-1][1]))


    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, deepRed, [XnY[0] ,XnY[1] ,block_size,block_size])

#put the random position gen into a function, to slim down amount of code, as the code in the function
#below is used more than once. This helps changing values and such
def randXYAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))
    return randAppleX,randAppleY

def message_to_screen(msg="Sample Text",color=black,y_displace=0, font=smallFont):


    textSurf = font.render(msg, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (display_width /2), (display_height /2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = block_size
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    #Put in function where the old code used to be. Used tuple to call variables
    randAppleX,randAppleY = randXYAppleGen()
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)

            #Parameters can be put to seperate lines if it makes reading easier
            #When putting in the defining variables again in the function,
            #They must go last, but the order in which all the variable are defined do not matter
            message_to_screen("Game Over", red, -50, mediumFont)
            message_to_screen("Press C to play again or Q to quit",black, 50,smallFont)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    #gameExit = True
                    #gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        direction = "right"
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change



        gameDisplay.fill(green)


        #Apple sprite has been put in
        gameDisplay.blit (appleImg,(randAppleX,randAppleY))
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY ,AppleThickness,AppleThickness])


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


        if randAppleX <= lead_x <= randAppleX+AppleThickness or randAppleX <= lead_x + block_size <= randAppleX+AppleThickness:
            if randAppleY <= lead_y <= randAppleY+AppleThickness or randAppleY <= lead_y + block_size <= randAppleY+AppleThickness:
                #Put in function here as well
                randAppleX,randAppleY = randXYAppleGen()
                #randAppleX = round(random.randrange(0, display_width - AppleThickness))
                #randAppleY = round(random.randrange(0, display_height - AppleThickness))
                snakeLength += 1


        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()