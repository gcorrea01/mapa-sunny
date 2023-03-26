import folium
import pandas as pd
import googlemaps

df = pd.read_excel('clientes_ativos.xlsx')
addresses = df['Endereco'].tolist()
types = df['Type'].tolist()
name = df['Nome'].tolist()

gmaps = googlemaps.Client(key='AIzaSyBL_LCsSUgsmZhNbKywyP32ZNcJz_xSdQg')

coordinates = []
for address in addresses:
    result = gmaps.geocode(address)
    if result:
        lat = result[0]['geometry']['location']['lat']
        lng = result[0]['geometry']['location']['lng']
        coordinates.append((lat, lng))

    else:
        print("Could not find location for: " + address)
        continue



map = folium.Map(location=[-30.05, -51.18], zoom_start=12)

#folium.TileLayer(
#    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#    attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
#).add_to(map)


for address, coord, type, name in zip(addresses, coordinates, types, name):
    if type == 'sale':
        color = 'purple'
    elif type == 'leasing':
        color = 'blue'
    folium.Marker(coord, popup=name, icon=folium.Icon(color=color)).add_to(map)




map.save("mymap.html")
