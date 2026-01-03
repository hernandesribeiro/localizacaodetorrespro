import pandas as pd
import re
def prepare_lt_dataframe(df):
    """
    Normaliza planilhas de LT mesmo quando não existem as colunas 'torre' e 'eixo'.
    """

    df = df.copy()

    # Forçar nomes das colunas para string
    df.columns = [str(c).strip().lower() for c in df.columns]

    # Identifica colunas por aproximação
    col_km = next((c for c in df.columns if "km" in c), None)
    col_torre = next((c for c in df.columns if "descrição localização" in c or "localização" in c), None)
    col_desc = next((c for c in df.columns if "descr" in c), None)

    if col_km is None:
        raise ValueError("Coluna de KM não encontrada na planilha.")

    if col_torre is None:
        raise ValueError("Coluna contendo as torres (ex.: 'Descrição Localização') não encontrada.")

    # Normaliza torre (texto vem misturado)
    df["torre"] = df[col_torre].astype(str).str.strip()
    df["torre_num"] = df["torre"].str.extract(r"(\d+)")  # extrai número se existir

    # km
    df["km"] = pd.to_numeric(df[col_km], errors="coerce")

    # Eixo (não existe) → preencher com None
    df["eixo"] = None

    # descrição (opcional)
    if col_desc:
        df["descricao"] = df[col_desc]
    else:
        df["descricao"] = None

    df = df.sort_values("km").reset_index(drop=True)
    return df
