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
            width=6, 
            style={'padding': '20px', 'background-color': 'white', 'border-radius': '21px', 'width':'34vw' },

    )