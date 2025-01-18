import plotly.express as px
from config import *


def draw_histogram(df, selected_disease):

    if selected_disease is None :
        selected_disease = DEFAULT_DISEASE1

    histogram_fig = px.histogram(
        df,
        x=selected_disease,
        nbins=30,
        title=f"Distribution of {selected_disease.split()[0]} in US counties (2024)",
        labels={selected_disease: "Prevalence (%)"},
        color_discrete_sequence=['#39da00']
    )

    histogram_fig.update_layout(
        yaxis_title="Number of counties",
        xaxis_title="Prevalence (%)",
        bargap=0.1,
    )

    return histogram_fig