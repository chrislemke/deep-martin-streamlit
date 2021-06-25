import streamlit as st


def app():
    st.title('Model overview')
    st.markdown('''Three different models are available. 
    They differ primarily in the data with which the respective model was pre-trained.
    All were trained on a dataset created from multiple datasets. These can be viewed [here](https://paperswithcode.com/task/text-simplification).''')
    st.subheader('BERT2BERT')
    st.write('''
    BERT2BERT is an encoder-decoder model which is based on [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) in both parts. 
    It was developed by Google in 2018, and trained on the BookCorpus and Wikipedia Corpus. 
    The version used here is the basic one with 12 layers, 768 hidden units, 12 attention heads and 110M parameters.
    ''')
    st.subheader('Newsela2Newsela')
    st.markdown('''
    This model is based on BERT and was fine-tuned with the help of the Newsela corpus. 
    The pre-trained model was published together with the article [here](https://github.com/chaojiang06/wiki-auto).  
    ''')
    st.subheader('RoBERTa2RoBERTa')
    st.markdown('''
    [RoBERTa](https://arxiv.org/abs/1907.11692): A Robustly Optimized BERT Pretraining Approach was developed by Facebook and is based on BERT. 
    It has the same size and differs accordingly only in the data set with which it was trained. 
    In addition, RoBERTa was trained with the CommonCrawl News dataset, the Web text corpus and the Stories from Common Crawl. 
    ''')
