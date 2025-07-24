import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# изучение структуры данных 
filename = 'mapping_global_datasets/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'mapping_global_datasets/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)



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




## Нанесение данных на карту.
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
        'colorbar': {'title': 'Magnitude'},
    }
}]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')