import streamlit as st
import time

import src.process
import src.default_texts


def app():
    st.title('Martin - the Heidegger countermovement')
    st.text('by Christopher Lemke')

    model_id = st.sidebar.selectbox(
        "Select the Model", ("Bert2Bert+",
                             "Newsela2Newsela+", "Roberta2Roberta+")
    )

    default_text = src.default_texts.quantum_mechanics
    st.write('### Add your text:')

    source_text = st.text_area(
        label='Maximum length 900 characters.', max_chars=900, height=270, value=default_text)

    do_sample_val = st.checkbox("Sampling", value=False)
    early_stopping_val = st.checkbox("Early stopping", value=False)

    num_beams_slider_val = st.slider(
        "Number of beams:", value=1, max_value=5, min_value=1)

    length_penalty_slider_value = st.slider(
        "Length penalty:", value=1.0, max_value=3.0, min_value=0.1)

    temperature_slider_val = st.slider(
        "Temperature:", value=1.0, max_value=10.0, min_value=0.1)

    no_repeat_ngram_siz_slider_value = st.slider(
        "Repeat n-gram size:", value=0, max_value=5, min_value=0)

    top_k_slider_val = st.slider(
        "Top-K:", value=50, max_value=50, min_value=0)

    clicked = st.button('Simplify')

    if clicked:

        processed_texts = src.process.process_text(
            source_text, model_id,
            temperature_slider_val,
            num_beams_slider_val,
            top_k_slider_val,
            do_sample_val,
            no_repeat_ngram_siz_slider_value,
            length_penalty_slider_value,
            early_stopping_val)

        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            latest_iteration.text(f'Martin is thinking ...🤔')
            bar.progress(i + 1)
            time.sleep(0.05)

        st.write('### Simplified text:')
        st.text_area(label=f'{model_id} says:',
                     value=processed_texts[0], height=270)
