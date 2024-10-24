import pygame
from PIL import Image
from car import Car
from pygame.locals import *
from pygame.math import Vector2
import random
import sys

TRACK = "assets/track.png"
COLLISION_MAP = "assets/collisionmap.jpg"

WINDOW_SIZE = (1400, 736)
FRAME_RATE = 120

Cars = []
POPULATION = 100

if __name__ == "__main__":

    pygame.init() #initialize pygame

    Cars = [Car((350, 680), collisionmap = Image.open(COLLISION_MAP).convert('1')) for i in range(POPULATION)]

    clock = pygame.time.Clock() # initialize clock

    screen = pygame.display.set_mode(WINDOW_SIZE) #set window size
    bg = pygame.image.load(TRACK)
    
    
    while True:
        #check if user exits
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        #draw background
        screen.blit(bg, Vector2(0,0))

        dt = clock.get_time()
        #update and draw cars
        [car.update(Vector2(-1, -0.5), random.random() ,dt) for car in Cars]
        [car.draw(screen) for car in Cars]
        
        clock.tick(FRAME_RATE)

        pygame.display.update()
        

        