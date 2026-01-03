import pandas as pd

def calcular_estatisticas(df):
    stats = {
        "total_amostras": len(df),
        "media_resistencia": df["Resistência Nominal (Ω)"].mean(),
        "media_diametro": df["Diâmetro"].mean() if "Diâmetro" in df else None,
        "torre_mais_recorrente": df["Número Operação"].mode()[0]
    }
    return stats

def filtrar_por_periodo(df, meses=12):
    df["Data"] = pd.to_datetime(df["Data"], errors="ignore")
    limite = df["Data"].max() - pd.DateOffset(months=meses)
    return df[df["Data"] >= limite]
