from dash import dcc, html
import dash_bootstrap_components as dbc
from config import *

def create_histograms_layout():
    return dbc.Container(
        fluid=True,
        className='histograms-container',
        children=[
            html.H1('Histograms', className='title', style={'textAlign': 'center'}),
            html.Label(
                'Select a disease:',
                className='label',
                style={'font-style': 'italic', 'font-weight': 'bold', 'textAlign': 'center'},
            ),
            dcc.Dropdown(
                id='disease-histogram-selector',
                options=[
                    {'label': 'Obesity', 'value': 'OBESITY_CrudePrev'},
                    {'label': 'Cancer', 'value': 'CANCER_CrudePrev'},
                    {'label': 'Stroke', 'value': 'STROKE_CrudePrev'},
                    {'label': 'Arthritis', 'value': 'ARTHRITIS_CrudePrev'},
                    {'label': 'Depression', 'value': 'DEPRESSION_CrudePrev'},
                    {'label': 'Diabetes', 'value': 'DIABETES_CrudePrev'},
                    {'label': 'High cholesterol', 'value': 'HIGHCHOL_CrudePrev'},
                    {'label': 'Teeth lost', 'value': 'TEETHLOST_CrudePrev'}
                ],
                value=DEFAULT_DISEASE,
                className='dropdown-container',
                clearable=False,
            ),
            dcc.Graph(id='disease-histogram'),
        ],
    )