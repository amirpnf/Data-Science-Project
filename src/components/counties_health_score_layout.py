from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *


def create_counties_health_score_layout():
    return dbc.Col(
            [
                html.H3('Map of Health Score by Counties (US)', className='title', style={'textAlign': 'center'}),
                dcc.Graph(id='choropleth-map-health-score'),
            ],

            width=6,
            style={'padding': '20px', 'background-color': 'white', 'border-radius':'21px', 'width':'34vw'}
    )