import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from src.utils.get_data import get_dataset, fetch_cdc_data
import pandas as pd
from src.utils.get_data import fetch_cdc_data
from src.utils.clean_dataset import clean_dataset
from src.utils.create_healthscore_dataset import create_health_score, create_health_score_by_state
from src.utils.create_state_dataset import create_state_dataset
from callbacks import init_callbacks
from config import *
import os

try:
    fetch_cdc_data(API_URL, fields=FIELDS)
    clean_dataset(RAW_DATA_DIR)
except Exception as e:
    clean_dataset(OFFLINE_DATA_DIR)

create_state_dataset()
df = pd.read_csv(CLEANED_DATA_DIR)

create_health_score()
create_health_score_by_state()

df_health = pd.read_csv(HEALTH_SCORE)
df_health_state = pd.read_csv(STATE_HEALTH_SCORE)
state_data = pd.read_csv(STATE_DATA_DIR)



app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ]
)

init_callbacks(app, df, df_health,df_health_state, state_data, GEOJSON_FILE)

if __name__ == '__main__':
    app.run_server(debug=DEBUG)
