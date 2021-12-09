from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self, num_points=50000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
while True:
    
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots() 
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input('end? (y/n): ')
    if keep_running == 'n':
        break
