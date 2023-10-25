import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'eq_data_30_day_m1.json'
with open(filename) as file:
    all_eq_data = json.load(file)

# readable_file = 'readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)
title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    mags.append(eq_dict['properties']['mag'])
    hover_texts.append(eq_dict['properties']['title'])

# Нанесения данных на карту
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

