from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

conclusion = 'Here goes the conclusion'

def create_guide_page_layout():
    return dbc.Container(
        fluid=True,
        className='guide-container',
        children=[
            html.H1('Guide and Conclusion', className='title', style={'textAlign' : 'center'}),
            html.P(conclusion, style={'textAlign' : 'center'})
        ]
    )