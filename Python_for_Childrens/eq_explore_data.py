from plotly.graph_objs import Layout
from plotly import offline
import json
filename = 'equshka.json'
with open(filename) as f:
    all_eq_data = json.load(f)
with open('readable_file.json', 'w') as f:
    json.dump(all_eq_data, f, indent=4)
all_eq_dicts = all_eq_data['features']
all_eq_dicts2 = all_eq_data

print(all_eq_dicts2['metadata']['title'])

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])
    print(mags)


data = [{'type': 'scattergeo', 'lon': lons, 'lat': lats,
         'marker': {'size': [5*mag for mag in mags],
                    'color': mags,
                    'colorscale': 'Viridis',
                    'reversescale': True,
                    'colorbar': {'title': 'Magnitude'}},
         'text': hover_texts}]
my_layout = Layout(title=all_eq_dicts2['metadata']['title'])
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

