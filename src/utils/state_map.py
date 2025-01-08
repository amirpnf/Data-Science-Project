import pandas as pd 
import plotly.express as px
from config import *
import json

def create_state_based_maps(data, disease1, disease2):
    if disease1 is None:
        disease1 = DEFAULT_DISEASE1
    if disease2 is None:
        disease2 = DEFAULT_DISEASE2

    with open(STATES_GEOJSON) as f:
        states = json.load(f)

    data['State name'] = data['State name'].str.strip().str.title()

    # Create the first map
    fig1 = px.choropleth(
        data, 
        geojson=states,
        locations='State name',
        featureidkey='properties.name',
        color=disease1,
        color_continuous_scale='RdYlGn_r',
        scope="usa",
        hover_name='State name',
        hover_data={
            'State name' : False
        }
    )

    # Create the second map
    fig2 = px.choropleth(
        data, 
        geojson=states,
        locations='State name',
        featureidkey='properties.name',
        color=disease2,
        color_continuous_scale='RdYlGn_r',
        scope="usa",
        hover_name='State name',
        hover_data = {
            'State name' : False
        }
    )

    fig1.update_layout(margin={"r":0, "t":30, "l":0, "b":0})
    fig2.update_layout(margin={"r":0, "t":30, "l":0, "b":0})

    return fig1, fig2