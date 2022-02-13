from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
frequencyes = []
max_result = die.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencyes.append(frequency)
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencyes)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'frequency of Result'}
my_layout = Layout(title='Results of rolling D{}'.format(die.num_sides), xaxis=x_axis_config, yaxis=y_axis_config)
fileik = 'd{}.html'.format(die.num_sides)
offline.plot({'data': data, 'layout': my_layout}, filename=fileik)
print(results, '\n', frequencyes)
