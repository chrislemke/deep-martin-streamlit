import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


def app():

    st.sidebar.title("About")
    st.sidebar.info('''
    Deep martin wants to help understand complicated and long texts better. 
    It uses transformer models trained using ~600k lines of simplified English. 
    ''')

    image = Image.open('heidegger.png')
    st.image(image, width=200)
    st.title('Deep Martin')
    st.title('Text simplification')
    st.subheader('the Heidegger countermovement')
    components.html('<br>')
    st.markdown(
        'Want to know more about Martin Heidegger? [Click here](https://en.wikipedia.org/wiki/Martin_Heidegger).')
