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
                width=6,  # Half the width of the row
            )