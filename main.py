import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from src.utils.get_data import get_dataset, fetch_cdc_data
from src.utils.draw_choropleth import generate_choropleth_map
from src.utils.draw_choropleth_test import generate_choropleth_map2
from src.utils.draw_histogram import draw_histogram
from src.utils.visualizations import plot_grouped_bar_chart
import pandas as pd
from src.utils.get_data import fetch_cdc_data
from src.utils.clean_dataset import clean_dataset
from src.utils.create_healthscore_dataset import create_health_score
from src.components.homepage import create_home_layout 
from src.components.choropleth_maps_page import create_choropleth_layout, create_choropleth_layout_health_score
from src.components.histograms import create_histograms_layout
from src.components.comparisons_page import create_comparisons_layout 
from src.components.guide import create_guide_page_layout
from src.components.comparisons_graph import create_comparisons_graph_layout
from src.utils.create_state_dataset import create_state_dataset
from callbacks import init_callbacks
from config import *

try:
    fetch_cdc_data(API_URL, fields=FIELDS)
except Exception as e:
    print(f"Error fetching data: {e}")

clean_dataset(RAW_DATA_DIR)
create_state_dataset()
df = pd.read_csv(CLEANED_DATA_DIR)
dfHealth = pd.read_csv(HEALTH_SCORE)
state_data = pd.read_csv(STATE_DATA_DIR)

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
try:
    create_health_score()
except Exception as e:
    print(f"Error healthScore: {e}")

# Layouts
home_layout = create_home_layout()
create_choropleth_layout_health_score()
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

init_callbacks(app, df, state_data, GEOJSON_FILE)

if __name__ == '__main__':
    app.run_server(debug=DEBUG)