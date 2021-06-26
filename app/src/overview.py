import streamlit as st



def app():
    st.title('Model overview')
    st.markdown('''Three different models are available. 
        They differ primarily in the data with which the respective model was pre-trained.
        All were trained on a dataset created from multiple datasets. These can be viewed [here](https://paperswithcode.com/task/text-simplification).''')

    st.write(''' 
     The idea behind *fine-tuning* the model is to transfer task-agnostic knowledge connected
     to a certain domain to a specific tasked based on this knowledge. The problem with general 
     text simplification, however, is that the associated knowledge is unspecifically large. 
     This can affect the predicted results. Specialization in a particular field, such as astronomy, 
     would counteract this, but at the expense of general text simplification.
    ''')

    st.subheader('Sequence2Sequence models')
    st.markdown(''' 
        The task of a sequence-to-sequence model is to map a input sequence $\mathbf{X}_{1:n}$
        to an output sequence $\mathbf{Y}_{1:m}$:
    ''')
    st.write(r'$p_{\theta_{{model}}}(\mathbf{Y}_{1:m} | \mathbf{X}_{1:n})$')
    st.write('\n')
    st.markdown(r'''
    They consist of an encoder layer and a decoder layer. The encoder
     (e.g. [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html)) 
    contextualize the input sequence $\mathbf{X}_{1:n}$ to $\mathbf{\overline{X}}_{1:n}$. 
    The decoder takes this contextualized input and an target sequence $\mathbf{Y}_{0:m-1}$ 
    and outputs a logit vectors $\mathbf{L}_{1:m}$:
    ''')
    st.write(
        r'$p_{\theta_{\text{dec}}}(\mathbf{Y}_{1:m} | \mathbf{\overline{X}}_{1:n})$')

    st.subheader('BERT2BERT')
    st.write('''
    BERT2BERT is an encoder-decoder model which is based on [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) in both parts. 
    BERT is an *encoder-only model* and was developed by Google in 2018, trained on the BookCorpus and Wikipedia Corpus. 
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
    Read [more](https://commoncrawl.org/) about common crawl. 
    ''')
