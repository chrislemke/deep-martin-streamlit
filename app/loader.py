from transformers import BartTokenizer, BartForConditionalGeneration, BartModel
import os
import streamlit as st


def load_model(identifier: str):
    if identifier == 'Distil BART':
        return _load_distil_bart_model()
    if identifier == 'Large Bart':
        return _load_large_bart_model()


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def _load_distil_bart_model():
    path = os.path.abspath(__file__ + '/../../models/distil_bart')
    tokenizer = BartTokenizer.from_pretrained(path, add_prefix_space=True)
    model = BartForConditionalGeneration.from_pretrained(
        path)
    return model, tokenizer


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def _load_large_bart_model():
    path = os.path.abspath(__file__ + '/../../models/large_bart')
    tokenizer = BartTokenizer.from_pretrained(path, add_prefix_space=True)
    model = BartForConditionalGeneration.from_pretrained(
        path)
    return model, tokenizer


def download_bart_model(identifier: str, save_path: str):
    tokenizer = BartTokenizer.from_pretrained(identifier)
    model = BartModel.from_pretrained(identifier)
    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)


if __name__ == '__main__':
    path = os.path.abspath(__file__ + '/../../models/large_bart')
    identifier = 'facebook/bart-large-cnn'
    download_bart_model(identifier, path)
