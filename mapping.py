import folium
import pandas as pd
volcanodata = pd.read_csv('Volcanoes.txt')
lat = list(volcanodata['LAT'])
lon = list(volcanodata['LON'])
name = list(volcanodata['NAME'])
elev = list(volcanodata['ELEV'])

map = folium.Map(location = [37.7749, -122.4194], zoom_start= 6, tiles = 'Stamen Terrain') #map object

fgv = folium.FeatureGroup(name = 'Volcanoes') #keeps all these features as one group

def elevcolor(elev): #color codes markers
    'takes an elevation (int) and returns a color (str)'
    if elev <= 1500:
        return 'green'
    elif elev <=3000:
        return 'orange'
    else:
        return 'red'

for lt, ln, nm, el in zip(lat, lon, name, elev): #volcano popups
    fgv.add_child(folium.CircleMarker(radius = 6, location = [lt, ln], popup = nm + '\n' + str(el)+ 'm', color= elevcolor(el), fill = True, fill_color = elevcolor(el), fill_opacity = .7)) #Circle markers
    #fg.add_child(folium.Marker(location = [lt, ln], popup = nm + '\n' + str(el)+ 'm', icon = folium.Icon(color= elevcolor(el)))) regular markers

fgp = folium.FeatureGroup(name = 'Population')

#adds country polygons
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
#geojson goes through all the features of each polygon
#style function takes a function, lambda was given
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <=10000000 else 
'orange' if x['properties']['POP2005'] <= 20000000 else
'red'}
)) 
map.add_child(fgv) 
map.add_child(fgp) # adds all features as group
map.add_child(folium.LayerControl())


map.save('VolcanoMap.html')