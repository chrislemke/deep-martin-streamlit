import src.simplifier
import src.overview
import src.how_to
import src.home
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
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.title("About")
st.sidebar.info('''
Deep martin wants to help understand complicated and long texts better. 
It uses transformer models trained using 600k lines of simplified English. 
''')
image = Image.open('profile_image.png')
st.sidebar.image(image, width=60)
st.sidebar.markdown('[Github](https://github.com/stoffy)')
st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/stoffy/)')
