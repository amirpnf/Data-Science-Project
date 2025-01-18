from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_state_health_score_layout():
    return dbc.Col(
            [
                html.H3('Health Score by state', className='title', style={'textAlign': 'center'}),
                dcc.Graph(id='choropleth-map-state-health-score'),
            ],

            width=6,
            style={'padding': '20px', 'background-color': 'white', 'border-radius':'21px', 'width':'34vw', 'box-shadow': '1px 2px 50px -24px rgba(0,0,0,0.32)'}  # Add some padding to the container
    )