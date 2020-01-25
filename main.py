#!/usr/bin python3

# Import the pygame module
import pygame
import time
import random

# # Import pygame.locais
# from pygame.locals import (
#         K_UP,
#         K_DOWN,
#         K_LEFT,
#         K_RIGHT,
#         K_ESCAPE,
#         KEYDOWN,
#         QUIT)

# Initialize pygame
pygame.init()

# Define constants for the color object
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CAR_WIDTH = 73

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pyGame") # Title
clock = pygame.time.Clock()

# Image
carImage = pygame.image.load('car.png')

# Define Things
def things(x, y, width, height, color):
    pygame.draw.rect(screen, color, [x, y, width, height])

# Define Moved Car
def car(x,y):
    screen.blit(carImage, (x,y))

# Text Object
def text_objects(text, font,):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

# Message Display
def message_display(text):
    largeText = pygame.font.Font('SIXTY.TTF', 115)
    textSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    screen.blit(textSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

# Crash Message
def crash():
    message_display('You Crashed')

# Main Loop
def game_loop():
    x = (SCREEN_WIDTH * 0.45)
    y = (SCREEN_HEIGHT * 0.8)
    x_change = 0
    car_speed = 0

    # Draw Thing
    thing_startx = random.randrange(0, SCREEN_WIDTH)
    thing_starty = -600
    thing_speed = 7
    thing_width = 20
    thing_height = 60

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #### MOVED CAR
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill(WHITE)
        
        things(thing_startx, thing_starty, thing_width, thing_height, BLACK)
        thing_starty += thing_speed
        car(x,y)

        if x > SCREEN_WIDTH - CAR_WIDTH or x < 0:
            crash()

        if thing_starty > SCREEN_HEIGHT:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, SCREEN_WIDTH)
        
        if y < thing_starty + thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_width or x + CAR_WIDTH > thing_startx and x + CAR_WIDTH < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
