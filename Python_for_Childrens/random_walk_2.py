from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self, num_points=500):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        self.values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 20, 50, 80])
            x_step = x_distance * x_direction
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 4, 10])
            y_step = y_distance * y_direction
            if x_step == 0 and y_step == 0:
                continue
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
            self.values.append(y)
            # self.values.append(y)
while True:
    
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16,10), dpi=128) 
    point_numbers = range(rw.num_points)
    for x in point_numbers:
        ax.plot(rw.x_values, rw.y_values,linewidth=0.1)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1000)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('end? (y/n): ')
    if keep_running == 'y':
        break
