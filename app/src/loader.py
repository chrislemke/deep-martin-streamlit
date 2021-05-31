from transformers import BartTokenizer, BartForConditionalGeneration, BartModel
import os
import streamlit as st


def load_model(identifier: str):
    if identifier == 'Distilled BART':
        return _load_distilled_bart_model()
    if identifier == 'Large Bart':
        return _load_large_bart_large_model()
    if identifier == 'Base Bart':
        return _load_bart_base_model()
    if identifier == 'El Barto':
        return _load_el_barto_model()


def _load_distilled_bart_model():
    path = os.path.abspath(__file__ + '/../../models/distilled_bart')
    tokenizer = BartTokenizer.from_pretrained(path, add_prefix_space=True)
    model = BartForConditionalGeneration.from_pretrained(
        path)
    return model, tokenizer


def _load_large_bart_large_model():
    path = os.path.abspath(__file__ + '/../../models/large_bart')
    tokenizer = BartTokenizer.from_pretrained(path, add_prefix_space=True)
    model = BartForConditionalGeneration.from_pretrained(
        path)
    return model, tokenizer

def _load_bart_base_model():
    path = os.path.abspath(__file__ + '/../../models/base_bart')
    tokenizer = BartTokenizer.from_pretrained(path, add_prefix_space=True)
    model = BartForConditionalGeneration.from_pretrained(
        path)
    return model, tokenizer

def _load_el_barto_model():
    path = os.path.abspath(__file__ + '/../../models/el_barto')
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
    path = os.path.abspath(__file__ + '/../../models/base_bart')
    identifier = 'facebook/bart-base'
    download_bart_model(identifier, path)
