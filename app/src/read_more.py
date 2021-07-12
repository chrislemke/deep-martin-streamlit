import streamlit as st


def app():
    st.title('More interesting stuff to read')
    st.write('Here are some nice articles to read:')
    st.markdown('[Attention Is All You Need](https://arxiv.org/abs/1706.03762)')
    st.markdown(
        '[BERT Rediscovers the Classical NLP Pipeline](https://arxiv.org/abs/1905.05950)')
    st.markdown(
        '[Leveraging Pre-trained Checkpoints for Sequence Generation Tasks](https://arxiv.org/abs/1907.12461)')
    st.markdown(
        '[Text Summarization with Pretrained Encoders](https://arxiv.org/abs/1908.08345)')
    st.markdown(
        '[Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/abs/1901.02860)')
    st.markdown(
        '[TransGAN: Two Pure Transformers Can Make One Strong GAN, and That Can Scale Up](https://arxiv.org/abs/2102.07074)')

