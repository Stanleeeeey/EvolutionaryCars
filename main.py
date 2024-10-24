import pygame
from PIL import Image
from car import Car
from pygame.locals import *
from pygame.math import Vector2
import sys
import utils
import genetic_alg

TRACK = "assets/track.png"
COLLISION_MAP = "assets/collisionmap.jpg"

WINDOW_SIZE = (1400, 736)
FRAME_RATE = 120

Cars = []
POPULATION = 100
PARENT_NUM = 10

if __name__ == "__main__":

    pygame.init() #initialize pygame
    clock = pygame.time.Clock() # initialize clock

    screen = pygame.display.set_mode(WINDOW_SIZE) #set window size
    bg = pygame.image.load(TRACK)
    
    genetic_controller = genetic_alg.GeneticAlghorithm(
        utils.exmaple_of_cost_function,
        POPULATION, 
        PARENT_NUM
    )

    i = 0
    while True:
        #check if user exits
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        #draw background
        screen.blit(bg, Vector2(0,0))

        dt = clock.get_time()



        #update and draw cars
        [car.update(dt) for car in genetic_controller.population]
        [car.draw(screen) for car in genetic_controller.population]

        genetic_controller.update()
        
        clock.tick(FRAME_RATE)

        pygame.display.update()
        

        i+=0.08