from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die(8)
die_2 = Die(8)
results = []
for roll_num in range(1000):
    result = die.roll() * die_2.roll()
    results.append(result)
frequencyes = []
max_result = die.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencyes.append(frequency)
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencyes)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'frequency of Result'}
my_layout = Layout(title='Results of rolling D{} and D{}'.format(die.num_sides, die_2.num_sides), xaxis=x_axis_config, yaxis=y_axis_config)
fileik = 'd{}_D{}.html'.format(die.num_sides, die_2.num_sides)
offline.plot({'data': data, 'layout': my_layout}, filename=fileik)
print(results, '\n', frequencyes)
