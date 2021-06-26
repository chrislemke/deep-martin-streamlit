import streamlit as st
from PIL import Image


def app():

    st.title('About the nerd mode')
    st.subheader('Intro')

    st.write('In encoder-decoder models, the decoder uses auto-regression to generate the next word. It is bases on the idea that the probability distribution of a sequence of tokens can be understood as product of conditional next word distributions.')
    x1 = r'''
        $$ 
        P(w_{1:T} | W_0 ) = \prod_{t=1}^T P(w_{t} | w_{1: t-1}, W_0)\text{, with }  w_{1: 0} = \emptyset 
        $$
        '''
    st.write(x1)
    st.write('The following functionalities can be applied to auto-regression. They all have different impact on the text generation.')
    st.markdown(
        'Checkout the Hugging Face [documentation](https://huggingface.co/transformers/main_classes/model.html#transformers.generation_utils.GenerationMixin.generate) for more information.')

    st.subheader('1. Sampling')
    st.write('''Shortly explained sampling is about taking the next word according to its conditional probability:''')
    x2 = r'''
    $$
    w_t \sim P(w | w_{1: t-1})
    $$
    '''
    st.write(x2)
    st.markdown(
        '''With **sampling** activated the prediction is not deterministic anymore.''')

    st.subheader('2. Number of beams')
    st.write('To find the next word in the sequence the model could simply pick the word with the highest probability(at each timestep 𝑡):')
    x3 = r'''
        $$ 
        w_t = argmax_{w}P(w | w_{1:t-1})
        $$
        '''
    st.write(x3)
    st.markdown('''This mechanism is called ** greedy search**. At first it sounds quite plausible: 
    In the process of finding the next the word, **greedy search** always picks the word with the highest probability. 
    Let’s assume after picking one we we end up with *"The", "very"* . Then it looks for the next word and has to choose 
    between *"honorable"* or *"evil"* - *"evil"* will have the higher probability so it would be picked. 
    The problem with **greedy search** is that later words could be hidden under lower probabilities of earlier words. 
    So even if *"evil"* has the higher probability the following probabilities are not taken in account.
    ''')

    st.markdown('''**Beam Search** reduces the risk of not taking higher hidden probabilities into account by looking 
    at the probabilities after the current step. By raising the number **beam search** looks further in the future. 
    It would have discovered that *"honorable"* would be the better pick - even if it had a lower probability. 
    Because it checked out the probability and saw that *"Optimus-Prime"* has a far higher probability than 
    *"Megatron"*. So **greedy search ** would have ended up with *"The very evil Optimus-Prime"* and **beam search** with: 
    *"The very honorable Optimus-Prime"*.
    ''')

    st.subheader('3. Length penalty')
    st.write('''Exponential penalty to the length. 1.0 means no penalty. 
    Set to values < 1.0 in order to encourage the model to generate shorter sequences, 
    to a value > 1.0 in order to encourage the model to produce longer sequences.''')
    st.subheader('4. Temperature')
    image = Image.open('temperature.jpg')
    st.image(image)
    st.write(
        'The left side could for example represent a temperature of ~ 0.5 the right side of ~ 1.1.')
    st.markdown('''The **temperature** has an effect on the sharpness of the probability distribution. 
    The lower the **temperature** the sharper the curve. The sharper the curve the more conservative the selected tokens.''')

    st.subheader('5. Repeat n-gram size')
    st.write('''This setting handles the repetition of n-grams. If this value is set to two no n-gram will be appear twice.''')

    st.subheader('6. Top-K')
    st.write('''In **Top-K-sampling** the *K* most likely next words are filtered out and and the probability mass is redisributed among those *Ks*.''')
