import folium
map = folium.Map(location = [37.7749, -122.4194], zoom_start= 6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map') #keeps all these features as one group

coordlist = [[37.7749, -122.4194], [37.8, -122.4194]]
for coordinate in coordlist:
    fg.add_child(folium.Marker(location = coordinate, popup = 'Test', icon = folium.Icon(color= 'green')))


map.add_child(fg) # adds all features as group
map.save('Map1.html')