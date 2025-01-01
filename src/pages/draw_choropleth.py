import folium


def generate_choropleth_map(df, disease):
    """_summary_

    Générer une carte choropleth avec Folium pour la maladie dont le nom
    est passé en argument

    Args:
        df (_type_): le dataset déjà chargé avec Pandas
        disease (_type_): le nom de maladie 
    """
    coords = [37.8, -96]
    us_counties = 'counties.geojson'
    m = folium.Map(location = coords, zoom_start=4)

    folium.Choropleth(
        geo_data=us_counties,
        name='US_Obesity',
        data=df,
        columns=['CountyName', disease],
        key_on='feature.properties.NAME',
        fill_color='RdYlGn_r',
        bins=[15, 25, 30, 40, 50, 60],
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Obesity'
    ).add_to(m)

    folium.LayerControl().add_to(m)

    map_html = str(m.get_root().render())
    return map_html