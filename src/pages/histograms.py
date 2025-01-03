from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_histograms_layout():
    return dbc.Container(
        fluid=True,
        className='histograms-container',
        children=[
            html.H1('Histograms', className='title', style={'textAlign': 'center'}),
            html.Label(
                'Select a disease:',
                className='label',
                style={'font-style': 'italic', 'font-weight': 'bold', 'textAlign': 'center'},
            ),
            dcc.Dropdown(
                id='disease-histogram-selector',
                options=OPTIONS,
                value=DEFAULT_DISEASE,
                className='dropdown-container',
                clearable=False,
            ),
            dcc.Graph(id='disease-histogram'),
        ],
    )