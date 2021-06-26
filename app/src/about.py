import streamlit as st
from PIL import Image



def app():
    image = Image.open('profile_image.jpg')
    st.image(image, width=100)
    
