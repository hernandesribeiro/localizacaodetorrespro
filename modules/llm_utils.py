from openai import OpenAI
import streamlit as st

@st.cache_resource
def load_llm():
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def perguntar_llm(model, pergunta):
    resposta = model.chat.completions.create(
        model=model,
        messages=[{"role":"user", "content": pergunta}]
    )
    return resposta.choices[0].message["content"]
