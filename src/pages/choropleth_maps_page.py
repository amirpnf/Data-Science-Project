from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_choropleth_layout():
    return dbc.Container(
        fluid=True,
        className='choropleth-container',
        children=[
            html.H1('Choropleth Maps', className='title', style={'textAlign': 'center'}),
            html.Label(
                'Select a disease:',
                className='label',
                style={'font-style': 'italic', 'font-weight': 'bold', 'textAlign': 'center'},
            ),
            dcc.Dropdown(
                id='disease-selector',
                options=OPTIONS,
                value=DEFAULT_DISEASE,
                className='dropdown-container',
                clearable=False,
            ),
            dcc.Graph(id='choropleth-map'),
        ],
    )