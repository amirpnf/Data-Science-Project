import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from src.pages.draw_histogram import draw_histogram
from src.pages.draw_choropleth import generate_choropleth_map
from src.utils.get_data import get_dataset
from src.utils.clean_dataset import clean_dataset

get_dataset()

# A call to clean_dataset() here ...

clean_dataset('data/raw/US_Counties_Health_Stats.csv')
df = pd.read_csv('data/cleaned/US_Counties_Health_Stats_CLEANED.csv')

app = dash.Dash(__name__)

DEFAULT_DISEASE = "OBESITY_CrudePrev"

app.layout = dbc.Container(
    fluid=True,
    className='app-container',
    children=[
        html.H1('Disease Analysis Across US Counties', className='title', style={'textAlign': 'center'}),
        html.Div(  # Wrap label and radio items in a Div for centering
            style={'textAlign': 'center', 'margin-bottom': '1rem'}, # Center align and add margin
            children=[
                html.Label(
                    'Select a disease:',
                    className='label',
                    style={'font-style': 'italic', 'font-weight': 'bold', 'textAlign': 'center'}, # Bold italic text
                ),
                dcc.Dropdown(
                    id='disease-selector',
                    options=[
                        {'label': 'Obesity', 'value': 'OBESITY_CrudePrev'},
                        {'label': 'Cancer', 'value': 'CANCER_CrudePrev'},
                        {'label': 'Stroke', 'value': 'STROKE_CrudePrev'},
                        {'label': 'Arthritis', 'value': 'ARTHRITIS_CrudePrev'},
                        {'label': 'Depression', 'value': 'DEPRESSION_CrudePrev'},
                        {'label': 'Diabetes', 'value': 'DIABETES_CrudePrev'},
                        {'label': 'High cholestrol', 'value': 'HIGHCHOL_CrudePrev'},
                        {'label': 'Teeth lost', 'value': 'TEETHLOST_CrudePrev'}
                    ],
                    value=DEFAULT_DISEASE,
                    className='dropdown-container',
                    clearable=False,
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='choropleth-map'), md=6, className='graph-container'),
                dbc.Col(dcc.Graph(id='disease-histogram'), md=6, className='graph-container'),
            ]
        ),
    ],
)

@app.callback(
    [Output('choropleth-map', 'figure'), Output('disease-histogram', 'figure')],
    [Input('disease-selector', 'value')]
)

def update_visualisation(selected_disease):
    
    choropleth_fig = generate_choropleth_map(df, selected_disease, 'counties.geojson')
    choropleth_fig.update_layout(coloraxis_colorbar=dict(title='Prevalence (%)'))

    histogram_fig = draw_histogram(df, selected_disease)

    return choropleth_fig, histogram_fig

if __name__ == '__main__':
    app.run_server(debug=True)