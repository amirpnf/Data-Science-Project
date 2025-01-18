import json
import pandas as pd
import plotly.express as px
from config import *

def generate_choropleth_map(df, disease, geojson_path):

    if disease is None :
        disease = DEFAULT_DISEASE1

    with open(geojson_path) as f:
        counties = json.load(f)
    
    df['CountyFIPS'] = df['CountyFIPS'].astype(str).str.zfill(5)

    fig = px.choropleth(
        df,
        geojson=counties,
        locations='CountyFIPS',
        featureidkey='properties.GEOID',
        color=disease,
        color_continuous_scale=CHOROPLETH_COLOR_SCALE,
        scope="usa",
        hover_name='CountyName',
        hover_data={
            'State name' : True,
            'Total Population' : True,
            'Total adult population' : True,
            'CountyFIPS' : False,
        }
    )

    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
    )
    
    return fig