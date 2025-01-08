import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from src.utils.get_data import fetch_cdc_data
from src.utils.clean_dataset import clean_dataset
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
state_data = pd.read_csv(STATE_DATA_DIR)

app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True, 
    external_stylesheets=[dbc.themes.UNITED]
)

app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ]
)

init_callbacks(app, df, state_data, GEOJSON_FILE)

if __name__ == '__main__':
    app.run_server(debug=DEBUG)