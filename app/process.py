import loader
import streamlit as st


def process_text(input_text, selected_model_id, length, temperature=0.7):
    max_length = int(len(input_text.split()) * (length / 100))

    model, tokenizer = loader.load_model(selected_model_id)
    inputs = tokenizer([input_text], max_length=1024, return_tensors='pt')
    output = model.generate(inputs['input_ids'], num_beams=5, max_length=max_length, early_stopping=True,
                            return_dict_in_generate=False, temperature=temperature)

    texts = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in output]
    return texts[0]


if __name__ == '__main__':
    text = 'This is a longer text, it should be shortened. '

    print(process_text(text, 'Distil BART', 120, 0.7))
