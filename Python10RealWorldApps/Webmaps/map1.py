"""
tiles = "Mapbox Bright"
Please use this instead:
tiles = "Stamen Terrain"
"""
import folium
map = folium.Map(location=[38, -99], zoom_start=6, tiles = "Stamen Terrain")
map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.save("Map2.html")
