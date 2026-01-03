import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def grafico_resistencia_hist(df):
    fig = px.histogram(df, x="Resistência Nominal (Ω)", nbins=30,title="Histograma de Resistência")
    return fig

def grafico_resistencia_tempo(df):
    df = df.copy()
    df["Data"] = pd.to_datetime(df["Data"])
    fig = px.line(df, x="Data", y="Resistência Nominal (Ω)",
                  title="Evolução Temporal da Resistência")
    return fig

def grafico_diametro(df):
    if "Diâmetro" not in df:
        return None
    fig = px.box(df, y="Diâmetro", title="Distribuição de Diâmetro")
    return fig
