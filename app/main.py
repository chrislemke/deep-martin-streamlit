import src.simplifier
import src.overview
import src.how_to
import src.home
import src.about
import streamlit as st

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

PAGES = {
    "Home": src.home,
    "Text simplification": src.simplifier,
    "About the nerd mode": src.how_to,
    "Model overview": src.overview,
    "About": src.about
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
