import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from src.utils.get_data import get_dataset, fetch_cdc_data
from src.utils.draw_choropleth import generate_choropleth_map
from src.utils.draw_histogram import draw_histogram
from src.utils.visualizations import plot_grouped_bar_chart
from src.utils.clean_dataset import clean_dataset
from src.components.homepage import create_home_layout 
from src.components.choropleth_maps_page import create_choropleth_layout
from src.components.histograms import create_histograms_layout
from src.components.comparisons_page import create_comparisons_layout 
from src.components.guide import create_guide_page_layout
from src.components.comparisons_graph import create_comparisons_graph_layout
from config import *

try:
    fetch_cdc_data(API_URL, fields=FIELDS)
except Exception as e:
    print(f"Error fetching data: {e}")

clean_dataset(RAW_DATA_DIR)
df = pd.read_csv(CLEANED_DATA_DIR)

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layouts
home_layout = create_home_layout()
choropleth_layout = create_choropleth_layout()
histograms_layout = create_histograms_layout()
comparisons_graph_layout = create_comparisons_graph_layout()
comparisons_layout = create_comparisons_layout()  
guide_page_layout = create_guide_page_layout()

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
    '''if pathname == '/choropleth':
        return choropleth_layout
    if pathname == '/histograms':
        return histograms_layout
    if pathname == '/comparisons-graph':
        return comparisons_graph_layout # A definir
    if pathname == '/comparisons-bar':
        return comparisons_layout  
    if pathname == '/guide':
        return guide_page_layout'''
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


@app.callback(
    Output('correlation-heatmap', 'figure'),
    [Input('disease1-comparison-selector', 'value'),
     Input('disease2-comparison-selector', 'value')]
)
def update_comparison(first_disease, second_disease):
    return plot_grouped_bar_chart(df, first_disease, second_disease)

if __name__ == '__main__':
    app.run_server(debug=DEBUG)
