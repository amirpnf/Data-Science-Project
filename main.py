import json

import folium
import pandas as pd

with open('counties.geojson', 'r') as f:
    geo_data = json.load(f)

coords = (40.264239,-100.787652)
pop_data = pd.read_csv('data/raw/PLACES__County_Data__GIS_Friendly_Format___2024_release_20241211.csv', sep=',')
counties = pop_data['OBESITY_CrudePrev']

map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

style_function = lambda x: {'fillColor': '#ffffff',
                            'color':'#000000',
                            'fillOpacity': 0.1,
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000',
                                'color':'#000000',
                                'fillOpacity': 0.50,
                                'weight': 0.1}

folium.Choropleth(
    geo_data=geo_data,                              # Fichier GeoJSON
    name='choropleth',
    data=pop_data,                                  # Données CSV
    columns=['CountyName', 'OBESITY_CrudePrev'],          # Colonne GeoJSON et métrique
    key_on='feature.properties.NAME',              # Correspondance avec le champ GeoJSON
    fill_color='Oranges',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Obesity Prevalence (%)'
).add_to(map)

NIL = folium.features.GeoJson(
    data = geo_data,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['NAME','NAME'],
        aliases=['County','Obesity percent'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
    )
)

map.add_child(NIL)
map.keep_in_front(NIL)
map.save(outfile='map.html')
