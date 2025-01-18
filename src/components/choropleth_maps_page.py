from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_choropleth_layout():
    return dbc.Col(
            [
                html.H3('Map of US Counties', className='title', style={'textAlign': 'center'}),
                html.Label(
                    'Select a disease:',
                    className='label',
                    style={'font-weight': 'bold', 'textAlign': 'center'},
                ),
                dcc.Dropdown(
                    id='disease-selector',
                    options=OPTIONS,
                    value=DEFAULT_DISEASE1,
                    className='dropdown-container',
                    clearable=False,
                ),
                dcc.Graph(id='choropleth-map'),
            ],
            width=6,  # Half the width of the row
            style={'padding': '20px', 'background-color': 'white', 'border-radius': '21px', 'width':'34vw', 'height': '30vw' },

    )

def create_choropleth_layout_health_score():
    return dbc.Col(
            [
                html.H3('Health Score', className='title', style={'textAlign': 'center'}),
                dcc.Graph(id='choropleth-map-health-score'),
            ],

            width=6,
            style={'padding': '20px', 'background-color': 'white', 'border-radius':'21px', 'width':'34vw', 'height':'30vw'}  # Add some padding to the container
    )

def create_choropleth_layout_state_health_score():
    return dbc.Col(
            [
                html.H3('Health Score by state', className='title', style={'textAlign': 'center'}),
                dcc.Graph(id='choropleth-map-state-health-score'),
            ],

            width=6,
            style={'padding': '20px', 'background-color': 'white', 'border-radius':'21px', 'width':'34vw', 'height':'30vw', 'box-shadow': '1px 2px 50px -24px rgba(0,0,0,0.32)'}  # Add some padding to the container
    )