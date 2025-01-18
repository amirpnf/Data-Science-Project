from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_maps_layout():
    return dbc.Row(
        [
            html.H4('State Comparison - Maps', className='title', style={'textAlign': 'center'}),
            dbc.Col(
                [
                    dcc.Dropdown(
                        id='disease-statemap-selector1',
                        options=OPTIONS,
                        value=DEFAULT_DISEASE1,
                        className='dropdown-container',
                        clearable=False,
                    ),
                    dcc.Graph(id='state-map1'),
                ],
                width=6,  # Half the width of the row
            ),
            dbc.Col(
                [
                    dcc.Dropdown(
                        id='disease-statemap-selector2',
                        options=OPTIONS,
                        value=DEFAULT_DISEASE2,
                        className='dropdown-container',
                        clearable=False,
                    ),
                    dcc.Graph(id='state-map2'),
                ],
                width=6,  # Half the width of the row
            ),
        ], style={'margin':'20px', 'background-color':'white', 'border-radius':'13px', 'padding-top':'10px', 'box-shadow': '1px 2px 50px -24px rgba(0,0,0,0.32)'},
    )
