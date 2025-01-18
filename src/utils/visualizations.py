import plotly.graph_objects as go

def plot_grouped_bar_chart(df, first_disease, second_disease):
    """
    Shows a grouped bar chart comparing the prevalence of two diseases across states.
    """
    if (not first_disease) or (not second_disease):
        return go.Figure()

    df_aggregated = df.groupby('State name', as_index=False).mean(numeric_only=True)

    df_aggregated = df_aggregated.sort_values(by=first_disease, ascending=False)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df_aggregated['State name'],
            y=df_aggregated[first_disease],
            name=first_disease,
            marker_color='#39da00'
        )
    )

    fig.add_trace(
        go.Bar(
            x=df_aggregated['State name'],
            y=df_aggregated[second_disease],
            name=second_disease,
            marker_color='#cea80d'
        )
    )
    
    fig.update_layout(
        title=f"Comparison of {first_disease} and {second_disease} by State",
        xaxis_title="State",
        yaxis_title="Prevalence (%)",
        barmode='group', 
        height=600,
        showlegend=True
    )

    return fig