import src.simplifier
import src.overview
import src.how_to
import src.home
import src.read_more
import streamlit as st
from PIL import Image

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
    "Read more": src.read_more
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

image = Image.open('profile_image.png')
st.sidebar.image(image, width=60)
st.sidebar.markdown('[Github](https://github.com/stoffy)')
st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/chrismlemke)')
