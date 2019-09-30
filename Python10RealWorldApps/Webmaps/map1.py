"""
tiles = "Mapbox Bright"
Please use this instead:
tiles = "Stamen Terrain"
"""
import folium
#Using FeatureGroup for Markers
map = folium.Map(location=[38, -99], zoom_start=6, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map2.html")

#Use a for loop to add list of coordinates
for coordinates in [[38,-99], [39,-99]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Marker1", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map3.html")
