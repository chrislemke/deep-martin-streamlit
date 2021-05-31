import app1
import app2
import streamlit as st

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

PAGES = {
    "Text simplification": app1,
    "Compare models": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Navigate", list(PAGES.keys()))
page = PAGES[selection]
page.app()
