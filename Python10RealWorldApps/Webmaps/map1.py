"""
tiles = "Mapbox Bright"
Please use this instead:
tiles = "Stamen Terrain"
"""
import folium
import pandas

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

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
coords = [[data["LAT"][i],data["LON"][i]] for i in range(len(data)) if data["LAT"][i]]
#print(data)

map = folium.Map(location=[40, -115], zoom_start=4, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
for c in coords:
    fg.add_child(folium.Marker(location=c, popup="Volcano", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map4a.html")

map = folium.Map(location=[40, -115], zoom_start=4, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
for y,x in zip(lat,lon):
    fg.add_child(folium.Marker(location=[y,x], popup="Volcano", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map4b.html")


#Our code so far...

import folium
import pandas

#function to calculate color based on mtn elevation
def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 < elevation < 3000:
        return 'orange'
    else:
        return 'red'

data = pandas.read_csv("Volcanoes.txt")
name = list(data["NAME"])
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[42.5, -115], zoom_start=4.5, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    #Marker(location, popup=None, tooltip=None, icon=None, draggable=False, **kwargs)
    #CircleMarker(location, radius=10, popup=None, tooltip=None, **kwargs)
    
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))
    #it seems that CircleMarker doesn't have 'icon' parameter for passing color function
    #use fill_color parameter for passing color function

#add GeoJson object
#GeoJson(data, style_function=None, highlight_function=None, name=None, overlay=True, 
#   control=True, show=True, smooth_factor=None, tooltip=None, embed=True)
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor':'yellow' 
                                                      if x['properties']['POP2005'] < 10000000 
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
                                                      else 'red'}))

map.add_child(fg)
map.save("Map4h.html")







