import streamlit as st
import src.process
import src.default_texts
import time


def app():
    st.title('El Barto - text simplification')
    st.text('by Christopher Lemke')

    model_id = st.sidebar.selectbox(
        "Select the Model", ("El Barto", "Base Bart", "Large Bart")
    )

    default_text = src.default_texts.identity
    st.write('### Add your text:')

    source_text = st.text_area(label='Maximum length 900 characters.', max_chars=900, height=270, value=default_text)

    percent_slider_val = 0
    temperature_slider_val = 0.0

    if model_id != 'El Barto':
        percent_slider_val = st.slider("Percentage of the original text:", value=50, min_value=20)
        temperature_slider_val = st.slider("Temperature:", value=0.7, max_value=2.0, min_value=0.1)

    clicked = st.button('Simplify')

    if clicked:

        if percent_slider_val == 0:
            percent_slider_val = 100
        if temperature_slider_val == 0.0:
            temperature_slider_val = 0.7

        processed_texts = src.process.process_text(source_text, model_id, percent_slider_val, temperature_slider_val)

        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            latest_iteration.text(f'Thinking ...🤔')
            bar.progress(i + 1)
            time.sleep(0.05)

        st.write('### Simplified text:')
        st.text_area(label=f'{model_id} says:', value=processed_texts[0], height=270)
