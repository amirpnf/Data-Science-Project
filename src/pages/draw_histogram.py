import plotly.express as px


def draw_histogram(df, selected_disease):

    histogram_fig = px.histogram(
        df,
        x=selected_disease,
        nbins=30,
        title=f"Distribution of {selected_disease.replace('_', ' ').split()[0].lower()} in US counties (2024)",  # Added closing parenthesis here
        labels={selected_disease: "Prevalence (%)"},
        color_discrete_sequence=['orange']
    )

    histogram_fig.update_layout(
        yaxis_title="Number of counties",
        xaxis_title="Prevalence (%)",
        bargap=0.1,
    )

    return histogram_fig