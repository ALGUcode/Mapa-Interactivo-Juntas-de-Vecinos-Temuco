import folium
import pandas as pd

data= pd.read_csv('JV.csv')

# Crear un mapa centrado en Temuco, Chile
mapa = folium.Map(location=[-38.726111, -72.560703], zoom_start=15)

# Añadir un marcador en una ubicación específica
for index, junta in data.iterrows():
    folium.Marker(
    location=[junta['Latitude'], junta['Longitude']],
    tooltip=junta['Nombre'],
    popup=folium.Popup(junta['Vigencia Directiva'], max_width=300)
).add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save("mapa_interactivo.html")