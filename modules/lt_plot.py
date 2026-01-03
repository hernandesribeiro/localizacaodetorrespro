import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from modules.km_utils import encontrar_torres

def plot_lt(df, km_busca=None, torre_central=None, titulo="LT"):

    alturas = np.random.uniform(20, 40, len(df))  # simulando altura
    fig, ax = plt.subplots(figsize=(13, 6))

    # plota linha base
    ax.plot(df["km"], alturas, marker="o", color="gray", linewidth=2)

    # destaca torre central
    if torre_central:
        idx = df.index[df["torre"] == torre_central]
        if len(idx) > 0:
            i = idx[0]
            ax.scatter(df.loc[i, "km"], alturas[i], s=200, c="red", label="Torre Central")
            ax.text(df.loc[i, "km"], alturas[i] + 1, f"Torre {torre_central}", color="red")

    # plota ponto por KM
    if km_busca is not None:
        km_list = df["km"].tolist()
        a, p = encontrar_torres(km_busca, km_list)

        if a is not None:
            # interpolação de altura
            frac = (km_busca - km_list[a]) / (km_list[p] - km_list[a])
            altura_interp = alturas[a] + frac * (alturas[p] - alturas[a])

            ax.scatter(km_busca, altura_interp, s=200, c="blue", label=f"KM {km_busca:.2f}")
            ax.text(km_busca, altura_interp + 1, f"KM {km_busca:.2f}", color="blue")

    ax.set_title(titulo)
    ax.set_xlabel("KM")
    ax.set_ylabel("Altura (m)")
    ax.grid(True)
    ax.legend()

    return fig
