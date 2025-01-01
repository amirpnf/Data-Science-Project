import folium
import pandas as pd 
import json


data = pd.read_csv("data/raw/County_data_2024.csv")
us_counties="counties.geojson"
print(data['OBESITY_CrudePrev'].describe())

with open(us_counties, 'r') as f:
    geojson_data = json.load(f)
geojson_keys = [feature['properties']['NAME'] for feature in geojson_data['features']]

missing = set(data["CountyName"].unique()) - set(geojson_keys)
print(missing)

coords = (37.97, -98.2)
m = folium.Map(coords, tiles = "cartodb positron", zoom_start = 5)

folium.Choropleth(
    geo_data=us_counties,
    name='US_Obesity',
    data=data,
    columns=['CountyName', 'OBESITY_CrudePrev'],
    key_on='feature.properties.NAME',
    fill_color='RdYlGn_r',
    bins=[15, 25, 30, 40, 50, 60],
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Obesity'
).add_to(m)

m.save(outfile='map.html')

print(data.describe())