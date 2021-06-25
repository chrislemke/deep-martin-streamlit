import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


def app():
    image = Image.open('heidegger.png')
    st.image(image, width=200)
    st.title('Deep Martin - text simplification')
    st.subheader('the Heidegger countermovement')
    st.write('by Christopher Lemke')
    components.html(
        '''<br><br>
         ''')
    st.markdown(
        'Want to know more about Heidegger? [Click here](https://en.wikipedia.org/wiki/Martin_Heidegger).')
