from dash import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from src.utils.draw_choropleth import generate_choropleth_map
from src.utils.draw_choropleth_test import generate_choropleth_map2, generate_choropleth_map_health_by_state
from src.utils.draw_histogram import draw_histogram
from src.utils.visualizations import plot_grouped_bar_chart
from src.utils.state_map import create_state_based_maps
from src.components.homepage import create_home_layout
from config import *

def init_callbacks(app, df, df_health,df_health_state, state_data, geojson_file):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        return create_home_layout()

    @app.callback(
        Output('choropleth-map', 'figure'),
        [Input('disease-selector', 'value')]
    )
    def update_choropleth(selected_disease):
        choropleth_fig = generate_choropleth_map(df, selected_disease, GEOJSON_FILE)
        choropleth_fig.update_layout(coloraxis_colorbar=dict(title='Prevalence (%)'))
        return choropleth_fig

    @app.callback(
        Output('choropleth-map-health-score', 'figure'),
        [Input('disease-selector', 'value')]  # Vous pouvez remplacer ce input avec celui que vous souhaitez
    )
    def update_choropleth_health_score(selected_disease):
        choropleth_fig3 = generate_choropleth_map2(df_health, GEOJSON_FILE)
        choropleth_fig3.update_layout(coloraxis_colorbar=dict(title='Health index'))
        return choropleth_fig3

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
        fig = plot_grouped_bar_chart(df, first_disease, second_disease)
        return fig

    @app.callback(
        [Output('state-map1', 'figure'), Output('state-map2', 'figure')],
        [Input('disease-statemap-selector1', 'value'), 
         Input('disease-statemap-selector2', 'value')]
    )
    def update_state_map(disease1, disease2):
        state_map1, state_map2 = create_state_based_maps(state_data, disease1, disease2)
        for fig in [state_map1, state_map2]:
            fig.update_layout(coloraxis_colorbar=dict(title='Prevalence (%)'))
        return state_map1, state_map2

    @app.callback(
        Output('choropleth-map-state-health-score', 'figure'),
        [Input('disease-selector', 'value')]  # Vous pouvez remplacer ce input avec celui que vous souhaitez
    )
    def update_choropleth_state_health_score(selected_disease):
        choropleth_fig3 = generate_choropleth_map_health_by_state(df_health_state, GEOJSON_FILE)
        choropleth_fig3.update_layout(coloraxis_colorbar=dict(title='Health index'))
        return choropleth_fig3
