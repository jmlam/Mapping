import folium
import pandas as pd
volcanodata = pd.read_csv('Volcanoes.txt')
lat = list(volcanodata['LAT'])
lon = list(volcanodata['LON'])
name = list(volcanodata['NAME'])
elev = list(volcanodata['ELEV'])

map = folium.Map(location = [37.7749, -122.4194], zoom_start= 6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map') #keeps all these features as one group

def elevcolor(elev): #color codes markers
    'takes an elevation (int) and returns a color (str)'
    if elev <= 2000:
        return 'green'
    elif elev <=3000:
        return 'orange'
    else:
        return 'red'

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location = [lt, ln], popup = nm + '\n' + str(el)+ 'm', icon = folium.Icon(color= elevcolor(el))))


map.add_child(fg) # adds all features as group
map.save('Map1.html')