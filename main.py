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
from src.utils.state_map import create_state_based_maps
from src.utils.create_state_dataset import create_state_dataset
from src.components.homepage import create_home_layout 
from config import *

try:
    fetch_cdc_data(API_URL, fields=FIELDS)
except Exception as e:
    print(f"Error fetching data: {e}")

clean_dataset(RAW_DATA_DIR)
create_state_dataset()
df = pd.read_csv(CLEANED_DATA_DIR)
state_data = pd.read_csv(STATE_DATA_DIR)

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layouts
home_layout = create_home_layout()

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

@app.callback(
    [Output('state-map1', 'figure'), Output('state-map2', 'figure')],
    [Input('disease-statemap-selector1', 'value'), Input('disease-statemap-selector2', 'value')]
)
def update_state_map(disease1, disease2):
    state_map1, state_map2= create_state_based_maps(state_data, disease1, disease2)
    state_map1.update_layout(coloraxis_colorbar=dict(title='Prevalence (%)'))
    state_map2.update_layout(coloraxis_colorbar=dict(title='Prevalence (%)'))
    return state_map1, state_map2


if __name__ == '__main__':
    app.run_server(debug=DEBUG)
