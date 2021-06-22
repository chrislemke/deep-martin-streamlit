import src.simplifier
import src.overview
import streamlit as st

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

PAGES = {
    "Text simplification": src.simplifier,
    "Model overview": src.overview
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Navigate", list(PAGES.keys()))
page = PAGES[selection]
page.app()
