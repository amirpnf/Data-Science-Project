from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *


def create_comparisons_graph_layout():
    return dbc.Col(
            [
            html.H4('Comparison - Barcharts', className='title', style={'textAlign': 'center'}),
            html.Label(
                'Select diseases to compare:',
                className='label',
                style={'font-style': 'italic', 'font-weight': 'bold', 'textAlign': 'center'},
            ),
            dcc.Dropdown(
                id='disease1-comparison-selector',
                options=OPTIONS,
                value=DEFAULT_DISEASE1,
                className='dropdown-container',
                clearable=False,
            ),
            dcc.Dropdown(
                id='disease2-comparison-selector',
                options=OPTIONS,
                value=DEFAULT_DISEASE2,
                className='dropdown-container',
                clearable=False,
            ),
            dcc.Graph(
                id='correlation-heatmap',
                config={'displayModeBar': True},
                style={'margin-top': '20px'}
            ),
            ],
            width=12,  # Full width for the heatmap
        )