import json
import pandas as pd
import plotly.express as px
from config import *

def generate_choropleth_map2(df, geojson_path):

    with open(geojson_path) as f:
        counties = json.load(f)
    
    df['CountyFIPS'] = df['CountyFIPS'].astype(str).str.zfill(5)

    fig = px.choropleth(
        df,
        geojson=counties,
        locations='CountyFIPS',
        featureidkey='properties.GEOID',
        color='Health Index',
        color_continuous_scale='RdYlGn',
        scope="usa", # Étant donné que nous étudions les États-Unis dans notre cas
        hover_name='CountyName',
        hover_data={
            'State name' : True,
            'Total Population' : True,
            'Total adult population' : True,
            'CountyFIPS' : False,
            'Health Index' : True,
        }
    )

    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
    )
    
    return fig