import plotly.graph_objects as go

def create_grouped_bar_charts(corr_matrix):
    
    diseases = corr_matrix.columns.tolist()
    data = []

    for disease in diseases:
        data.append(
            go.Bar(
                name=disease,
                x=diseases,
                y=corr_matrix[disease].values,
                text=corr_matrix[disease].values,
                textposition='auto'
            )
        )

    fig = go.Figure(data=data)
    fig.update_layout(
        title='Relationships between Diseases (Grouped Bar Chart)',
        xaxis_title='Diseases',
        yaxis_title='Correlation Strength',
        barmode='group',
        template='plotly_white'
    )

    return fig