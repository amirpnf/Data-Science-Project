import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from src.utils.get_data import get_dataset
from src.pages.draw_choropleth import generate_choropleth_map

get_dataset()

# A call to clean_dataset() here ...

df = pd.read_csv("data/cleaned/US_Counties_Health_Stats.csv")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Disease Analysis Across US Counties", style={"textAlign" : "center"}),

    html.Label("Select a disease :"),
    dcc.RadioItems(
        id='disease-selector',
        options=[
            {'label' : 'Obesity', 'value' : 'OBESITY_CrudePrev'},
            {'label' : 'Cancer', 'value' : 'CANCER_CrudePrev'},
            {'label' : 'Stroke', 'value' : 'STROKE_CrudePrev'}
        ],
        value='OBESITY_CrudePrev',
        inline=True
    ),

    dcc.Graph(id='choropleth-map'),

    dcc.Graph(id='disease-histogram')
])

@app.callback(
    [Output('choropleth-map', 'figure'), Output('disease-histogram', 'figure')],
    [Input('disease-selector', 'value')]
)

def update_visualisation(selected_disease):
    
    '''choropleth_fig = px.choropleth(
        df, 
        geojson='counties.geojson',
        locations='CountyFIPS',
        color=selected_disease,
        hover_name='CountyName',
        title=f"Choropleth map : {selected_disease.replace('_', ' ')}",
        color_continuous_scale="Viridis",
        scope='usa'
    )
    choropleth_fig.update_geos(fitbounds="locations", visible=False)'''
    choropleth_html = generate_choropleth_map(df, selected_disease)
    choropleth_fig = html.Iframe(
        srcDoc=choropleth_html,
        style={"width": "100%", "height": "600px", "border": "none"}
    )

    histogram_fig = px.histogram(
        df, 
        x=selected_disease,
        nbins=30, 
        title=f"Distribution of {selected_disease.replace('_', ' ')}",
        labels={selected_disease : "Prevalence"}
    )

    return choropleth_fig, histogram_fig

if __name__ == "__main__":
    app.run_server(debug=True)