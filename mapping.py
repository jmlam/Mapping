import folium
import pandas as pd
volcanodata = pd.read_csv('Volcanoes.txt')
lat = list(volcanodata['LAT'])
lon = list(volcanodata['LON'])
name = list(volcanodata['NAME'])

map = folium.Map(location = [37.7749, -122.4194], zoom_start= 6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map') #keeps all these features as one group

for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(location = [lt, ln], popup = nm, icon = folium.Icon(color= 'green')))


map.add_child(fg) # adds all features as group
map.save('Map1.html')