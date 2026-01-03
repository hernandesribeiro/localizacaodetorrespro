import folium
from streamlit_folium import st_folium

def gerar_mapa(df_lt):
    m = folium.Map(location=[-15.89, -47.99], zoom_start=5)

    for _, row in df_lt.iterrows():
        if "latitude" in row and "longitude" in row:
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=f"Torre {row['torre']}"
            ).add_to(m)

    return m
