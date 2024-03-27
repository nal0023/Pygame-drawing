#Reskin Notes: Changed all sin() to cos(), screen.fill(black) is now screen.fill(white)
# Value on line 64 has been chnaged to 3.14.

import pygame
import pygame.gfxdraw
import math

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock ()

white = (255,255, 255)
black = (0,0,0)

running = True

plusX = screenWidth // 2
plusY = screenHeight // 2

def draw_flat_line(screen, x1, y1, length, color):
    for x in range (x1, x1 + length):
        pygame.gfxdraw.pixel(screen, x, y1, color)

def draw_vertical_line (screen, x1, y1, length, color):
    for y in range (y1, y1 +length):
        pygame.gfxdraw.pixel(screen, x1, y, color)

def draw_plus_sign(screen, x, y, size, color):
    draw_flat_line (screen, x -(size//2), y, size, color)
    draw_vertical_line(screen, x, y -(size//2), size, color)

centerPoint = (screenWidth // 2, screenHeight // 2)

#Add a new list before our loop starts
cursorList = []

#set the start points to the center of the screen
plusX = screenWidth //2
plusY = screenHeight //2

while running:
    screen.fill(white)
    #every loop, draw the plus sign again at new position
    draw_plus_sign(screen, plusX, plusY, 15, white)
    #loop over each our cursor position. If empty it skips
    for i,plusSign in enumerate(cursorList):
        rR = math.cos(i* .01) * 127 +128
        rG = math.cos(i* .01 +5) * 127 +128
        rB = math.cos(i * .01 +10) * 127 +128

        #Generate a separate fader for all of them to be scaled
        fader = (math.cos(i*.02) + 1) /2
        rR =rR *fader
        rG =rG * fader
        rB = rB * fader
        #try changing the value below from .005 to 5.2
        sizer = int(math.cos(i*3.14) * 35 + 35)
        draw_plus_sign(screen, plusSign[0], plusSign[1], sizer, (rR, rG, rB))
    
    #get the list of keys that are pressed/not pressed
    key = pygame.key.get_pressed()
    #check if our key is pressed, change the right value
    if key[pygame.K_SPACE]:
        #takes current position of cursor and creates a list with xy
        newPlace = [plusX, plusY]
        #add that list to our cursorList
        cursorList.append(newPlace)
        
    if key[pygame.K_UP]:
        plusY = plusY -1
    elif key [pygame.K_DOWN]:
        plusY = plusY + 1
    if key [pygame.K_LEFT]:
        plusX = plusX - 1
    elif key [pygame.K_RIGHT]:
        plusX = plusX + 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()#This is how we update the screen while drawing
