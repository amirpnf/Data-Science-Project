from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_histograms_layout():
    return dbc.Col(
                [
                    html.H3('Histograms', className='title', style={'textAlign': 'center'}),
                    html.Label(
                        'Select a disease:',
                        className='label',
                        style={'font-weight': 'bold', 'textAlign': 'center'},
                    ),
                    dcc.Dropdown(
                        id='disease-histogram-selector',
                        options=OPTIONS,
                        value=DEFAULT_DISEASE1,
                        className='dropdown-container',
                        clearable=False,
                    ),
                    dcc.Graph(id='disease-histogram'),
                ],
                width=6, style={'padding':'20px', 'border-radius': '13px', 'background-color': 'white', 'margin':'20px', 'box-shadow': '1px 2px 50px -24px rgba(0,0,0,0.32)'},
            )