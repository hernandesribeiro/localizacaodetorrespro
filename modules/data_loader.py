# modules/data_loader.py
import pandas as pd
import streamlit as st
from io import BytesIO


@st.cache_data
def load_sheet_from_path_or_buffer(path_or_buffer, sheet_name):
    if isinstance(path_or_buffer, str):
        return pd.read_excel(path_or_buffer, sheet_name=sheet_name)
    else:
        path_or_buffer.seek(0)
        data = path_or_buffer.read()
        return pd.read_excel(BytesIO(data), sheet_name=sheet_name)
