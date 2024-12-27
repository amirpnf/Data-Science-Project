import pandas as pd 
import plotly.express as px

data = pd.read_csv("data/raw/County_data_2024.csv")
#data_sorted = data.sort_values("OBESITY_CrudePrev", ascending=False)
fig = px.histogram(data,
                   x="OBESITY_CrudePrev",
                   nbins=20,
                   text_auto=True,
                   title='Obesity Rates by County',
                   labels={'OBESITY_CrudePrev':'Obesity Rate',
                           'count':'Number of Counties'},)

fig.update_layout(
    height=600,
    bargap=0.2,  # Gap between bars
    xaxis_title="Obesity Rate (%)",
    yaxis_title="Number of Counties",
    hoverlabel=dict(
        bgcolor="white",
        font_size=16
    )
)
fig.update_traces(
    hovertemplate="Obesity Rate: %{x:.1f}%<br>Number of Counties: %{y}<extra></extra>"
)
fig.show()