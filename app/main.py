import streamlit as st

import process
import time

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('El Barto - text simplification')
st.text('by Christopher Lemke')

model_id = st.sidebar.selectbox(
    "Select the Model", ("Distil BART", "Large Bart")
)

st.write('### Add your text:')

default_text = 'The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'

source_text = st.text_area(label='Maximum length 1024 words.', max_chars=7500, height=250, value=default_text)
percent_slider_val = st.slider("Percentage of the original text:", value=50, min_value=20)
temperature_slider_val = st.slider("Temperature:", value=0.7, max_value=1.0, min_value=0.1)

clicked = st.button('Simplify')

if clicked:

    processed_text = process.process_text(source_text, model_id, percent_slider_val, temperature_slider_val)

    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Thinking ...')
        bar.progress(i + 1)
        time.sleep(0.1)

    st.write('### Simplified text:')
    st.text_area(label='El Barto says:', value=processed_text, height=250)
