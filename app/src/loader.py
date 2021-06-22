from transformers import BertTokenizerFast, EncoderDecoderModel, RobertaTokenizerFast
import os
import streamlit as st


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_model(identifier: str):
    if identifier == 'Bert2Bert+':
        return __load_bert2bert_big_model()
    if identifier == 'Newsela2Newsela+':
        return __load_newsela2newsela_big_model()
    if identifier == 'Roberta2Roberta+':
        return __load_roberta2roberta_big_model()


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def __load_roberta2roberta_big_model():
    path = os.path.abspath(__file__ + '/../../models/roberta2roberta_big')
    tokenizer = RobertaTokenizerFast.from_pretrained(path)
    model = EncoderDecoderModel.from_pretrained(path)
    return model, tokenizer


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def __load_bert2bert_big_model():
    path = os.path.abspath(__file__ + '/../../models/bert2bert_big')
    tokenizer = BertTokenizerFast.from_pretrained(path)
    model = EncoderDecoderModel.from_pretrained(path)
    return model, tokenizer


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def __load_newsela2newsela_big_model():
    path = os.path.abspath(__file__ + '/../../models/newsela2newsela_big')
    tokenizer = BertTokenizerFast.from_pretrained(path)
    model = EncoderDecoderModel.from_pretrained(path)
    return model, tokenizer
