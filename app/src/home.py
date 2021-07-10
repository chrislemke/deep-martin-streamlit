import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


def app():

    st.sidebar.title("About")
    st.sidebar.info('''
    Deep Martin is a project consisting of several ML models. 
    All of them are Sequence2Sequence transformer. 
    Primarily they differ in terms of the data they were pre-trained with. 
    ''')

    image = Image.open('heidegger.png')
    st.image(image, width=200)
    st.title('Deep Martin')
    st.title('Text simplification')
    st.subheader('for the democratization of knowledge ')
    components.html('<br>')
    st.markdown(
        'Want to know more about Martin? [Click here](https://en.wikipedia.org/wiki/Martin_Heidegger).')
