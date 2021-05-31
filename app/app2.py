import streamlit as st
import pandas as pd


def app():
    df = pd.read_excel('models.xlsx')
    df = df[['name', 'architectures', 'fine_tuned', 'activation_function', 'd_model', 'Attention_heads',
             'max_position_embeddings']]
    st.dataframe(df)
