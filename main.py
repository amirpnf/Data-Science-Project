import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from src.utils.get_data import get_dataset, fetch_cdc_data
from src.utils.draw_choropleth import generate_choropleth_map
from src.utils.draw_histogram import draw_histogram
from src.utils.clean_dataset import clean_dataset
from src.pages.homepage import create_home_layout 
from src.pages.choropleth_maps_page import create_choropleth_layout
from src.pages.histograms import create_histograms_layout
from config import *

try:
    data = fetch_cdc_data(API_URL, fields=FIELDS)
except Exception as e:
    print(f"Error fetching data: {e}")

# A call to clean_dataset() here ...
clean_dataset(data)

# The cleaned dataset will be saved in a new folder called cleaned
df = pd.read_csv(CLEANED_DATA_DIR)

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Home page layout
home_layout = create_home_layout()

# Choropleth page layout
choropleth_layout = create_choropleth_layout()

# Histograms' page layout
histograms_layout = create_histograms_layout()

# App layout
app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ]
)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/choropleth':
        return choropleth_layout
    
    if pathname == '/histograms':
        return histograms_layout

    return home_layout


@app.callback(
    Output('choropleth-map', 'figure'),
    [Input('disease-selector', 'value')]
)
def update_choropleth(selected_disease):
    choropleth_fig = generate_choropleth_map(df, selected_disease, GEOJSON_FILE)
    choropleth_fig.update_layout(coloraxis_colorbar=dict(title='Prevalence (%)'))
    return choropleth_fig


@app.callback(
    Output('disease-histogram', 'figure'),
    [Input('disease-histogram-selector', 'value')]
)
def update_histogram(selected_disease):
    return draw_histogram(df, selected_disease)

if __name__ == '__main__':
    app.run_server(debug=DEBUG)