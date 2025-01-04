from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_home_layout():
    return dbc.Container(
        fluid=True,
        className='home-container',
        children=[
            html.H1('Disease Analysis Across US Counties', className='title', style={'textAlign' : 'center'}),
            html.P("Bienvenue! Utilisez les buttons suivants afin d'accéder aux différentes pages", style={'textAlign' : 'center'}),
            dbc.Row(
                className='button-row',
                children=[
                    dbc.Col(
                        dbc.Button('Choropleth Maps', href='/choropleth', color='primary', size='lg'),
                        width='auto',
                        style={'textAlign' : 'center'},
                        className='custom-button'
                    ),
                    dbc.Col(
                        dbc.Button('Histograms', href='/histograms', color='secondary', size='lg'),
                        width='auto',
                        style={'textAlign' : 'center'},
                        className='custom-button'
                    ),
                    dbc.Col(
                        dbc.Button('Comparisons', href='/comparisons', color='secondary', size='lg'),
                        width='auto',
                        style={'textAlign' : 'center'},
                        className='custom-button'
                    ),
                    dbc.Col(
                        dbc.Button('Guide and conclusion', href='/guide', color='secondary', size='lg'),
                        width='auto',
                        style={'textAlign' : 'center'},
                        className='custom-button'
                    )
                ],
                justify='center'
            )
        ]
    )