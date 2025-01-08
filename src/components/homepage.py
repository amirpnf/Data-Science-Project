from dash import dcc, html
import dash_bootstrap_components as dbc
from src.pages.choropleth_maps_page import create_choropleth_layout
from src.pages.histograms import create_histograms_layout
from src.pages.comparisons_graph import create_comparisons_graph_layout
from config import *

def create_home_layout():
    return dbc.Container(
        fluid=True,
        className='homepage-container',
        children=[
            # Row 1: Choropleth Map and Histogram
            dbc.Row(
                [
                    # Choropleth Map
                    create_choropleth_layout,
                    # Histogram
                    create_histograms_layout,
                ],
                align='center',  # Vertically center the columns
                style={'marginBottom': '20px'}
            ),
            # Row 2: Correlation Heatmap
            dbc.Row(
                [
                    create_comparisons_graph_layout
                ],
                align='center',
            ),
        ],
        style={'padding': '20px'}  # Add some padding to the container
    )
