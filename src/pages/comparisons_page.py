from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_comparisons_layout():
    return dbc.Container(
        fluid=True,
        className='comparisons-container',
        children=[
            html.H1('Comparisons', className='title', style={'textAlign': 'center'}),
            html.Label(
                'Select diseases to compare:',
                className='label',
                style={'font-style': 'italic', 'font-weight': 'bold', 'textAlign': 'center'},
            ),
            dcc.Dropdown(
                id='disease-comparison-selector',
                options=OPTIONS,
                value=[DEFAULT_DISEASE],
                multi=True,
                className='dropdown-container',
                clearable=False,
            ),
            dcc.Graph(
                id='correlation-heatmap',
                config={'displayModeBar': True},
                style={'margin-top': '20px'}
            ),
        ],
    )
