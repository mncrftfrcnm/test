from plotly.graph_objs import Layout
from plotly import offline
import json
import csv
filename = 'world_fires_1_day.csv'
lats, lons, hover_texts, mags = [], [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
            lats.append(row[0])
            lons.append(row[1])
            mags.append(float(row[4]))
            hover_texts.append(row[-1])
print(mags)

data = [{'type': 'scattergeo', 'lon': lons, 'lat': lats,
         'marker': {'size': [5*mag for mag in mags],
                    'color': mags,
                    'colorscale': 'Viridis',
                    'reversescale': True,
                    'colorbar': {'title': 'Magnitude'}},
         'text': hover_texts}]
my_layout = Layout(title='fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

