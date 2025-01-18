from click import style
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.choropleth_maps_page import create_choropleth_layout
from src.components.state_health_score_layout import create_state_health_score_layout
from src.components.counties_health_score_layout import create_counties_health_score_layout
from src.components.histograms import create_histograms_layout
from src.components.comparisons_graph import create_comparisons_graph_layout
from src.components.state_map_layout import create_maps_layout
from config import *

def create_home_layout():
    return dbc.Container(
        fluid=True,
        className='homepage-container',
        children=[
            dbc.Row([

                dbc.Col([
                    html.Div([
                        html.H2("Dashboard", className="mb-4", style={'position':'fixed'}),

                        html.Div([
                            html.H4("Informations"),
                            html.P("Comprehensive Health Analysis of US Counties and States")
                        ], className="mt-4 p-3 text-white rounded", style={'background-color': '#39da00', 'width': '13vw', 'position':'fixed', 'top':'100px'}),
                        html.Div([
                            html.H4("Authors"),
                            html.P("BRAVARD Lorenzo - POUYANFAR AmirHossein - E3FI - 1l")
                        ], className="mt-4 p-3 text-white rounded", style={'background-color': '#39da00', 'width': '13vw', 'position':'fixed', 'bottom':'50px', 'font-size':'0.9em'}),
                    ], className="sidebar p-4 h-100", style={'background-color': 'white'}),
                ], width=2, style={'padding-left': '0', 'padding-right': '0','box-shadow': '-5px 2px 15px 5px rgba(0,0,0,0.32)', 'z-index':'5'}),
                dbc.Col([
                    dbc.Row(
                        [
                            # Choropleth Map
                            dbc.Row([ create_choropleth_layout(),
                            create_counties_health_score_layout(),

                            ],style={'background-color': 'white', 'margin': '20px', 'flex-direction':'row','justify-content': 'space-evenly', 'border-radius': '13px', 'box-shadow': '1px 2px 50px -24px rgba(0,0,0,0.32)'}),

                            # Histogram
                            create_histograms_layout(),
                        ],
                        align='center',
                        style={'margin': '20px','marginBottom': '20px', 'display':'flex', 'flexDirection': 'row', 'flex-flow': 'wrap', 'justify-content': 'space-around', 'margin-top': '10px'}
                    ),
                    dbc.Row(
                        [
                            create_comparisons_graph_layout(),
                            create_maps_layout(),
                            create_state_health_score_layout(),
                        ],
                        align='center', style={'margin':'20px', 'display':'flex', 'justify-content':'center'}
                    ),
                ],
                style={'background-color':'#e7f9ec', 'padding-left':'0'}
            )],),
 ]),