import json
import pandas as pd
import plotly.express as px
from config import *

def generate_choropleth_map_health(df, geojson_path):

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


def generate_choropleth_map_health_by_state(df_health_state, geojson_path):
    with open(STATES_GEOJSON) as f:
        states = json.load(f)

    df_health_state['State name'] = df_health_state['State name'].astype(str).str.zfill(5)

    fig = px.choropleth(
        df_health_state,
        geojson=states,
        locations='State name',
        featureidkey='properties.name',
        color='Health Index',
        color_continuous_scale='RdYlGn',
        scope="usa",  # Étant donné que nous étudions les États-Unis dans notre cas
        # hover_name='State name',
        hover_data={
            'State name': True,
            'Total Population': True,
            'Total adult population': True,
            'Health Index': True,
        }
    )

    fig.update_layout(
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
    )

    return fig