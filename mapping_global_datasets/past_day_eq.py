import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'mapping_global_datasets/data/all_day.json'
with open(filename) as f : 
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts),'\n')

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0]) 
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# printing first 10 mags to confirm that all correct
print(mags[:10])
print(lons[:10])
print(lats[:10])

# Нанесение данных на карту.
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats, 
    'text': hover_texts,
    'marker': {
        'size': [max(1, 5 * mag) if mag is not None else 1 for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitudes'},
    }
}]

my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='all_day_eq.html')
