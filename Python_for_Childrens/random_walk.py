from random import choice
class RandomWalk():
    def __init__(self,num_points=90000):
        self.num_points = num_points
        self.x_values = [0]
        self.x_values = [0]
        self.x_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            