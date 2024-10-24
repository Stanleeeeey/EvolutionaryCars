from car import Car
from PIL import Image
from typing import Callable

class GeneticAlghorithm:
    def __init__(self, cost_function : Callable[[Car], int], population_size, parents_num):
        self.cost_function =  cost_function
        
        
        self.population_size = population_size
        self.parents_num = parents_num
        self.population = [Car((350, 680), collisionmap = Image.open("assets/collisionmap.jpg").convert('1')) for i in range(population_size)]


    def select_parents(self):
        
        costs = [self.cost_function(i) for i in self.population]

        costs.sort()

        ans = []
        for i in costs[:self.parents_num]:
            ans.append(self.population[costs.index(i)])

        return ans

    def update(self,):
        self.select_parents()