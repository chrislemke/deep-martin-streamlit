import src.loader


def process_text(
        input_text,
        selected_model_id,
        temperature_slider_val,
        num_beams_slider_val,
        top_k_slider_val,
        do_sample_val,
        no_repeat_ngram_size_slider_value,
        length_penalty_slider_value,
        early_stopping):

    print('\n')
    print('selected_model_id:', selected_model_id)
    print('temperature_slider_val:', temperature_slider_val)
    print('num_beams_slider_val:', num_beams_slider_val)
    print('top_k_slider_val:', top_k_slider_val)
    print('do_sample_val:', do_sample_val),
    print('no_repeat_ngram_size_slider_value:',
          no_repeat_ngram_size_slider_value)
    print('length_penalty_slider_value:', length_penalty_slider_value)
    print('early_stopping:', early_stopping)

    model, tokenizer = src.loader.load_model(selected_model_id)
    text_length = len(input_text.split())
    max_length = int(text_length + (text_length * 0.2))
    min_length = int(text_length * 0.5)

    inputs = tokenizer([input_text], padding='max_length',
                       max_length=max_length + 15, truncation=True, return_tensors='pt')

    model.config.decoder_start_token_id = tokenizer.cls_token_id
    model.config.eos_token_id = tokenizer.sep_token_id
    model.config.pad_token_id = tokenizer.pad_token_id
    model.config.vocab_size = model.config.encoder.vocab_size

    output = model.generate(inputs['input_ids'],
                            max_length=max_length,
                            min_length=min_length,
                            num_beams=num_beams_slider_val,
                            no_repeat_ngram_size=no_repeat_ngram_size_slider_value,
                            length_penalty=length_penalty_slider_value,
                            temperature=temperature_slider_val,
                            early_stopping=early_stopping,
                            top_k=top_k_slider_val,
                            do_sample=do_sample_val
                            )

    text = tokenizer.batch_decode(
        output, skip_special_tokens=True)
    return text


if __name__ == '__main__':
    import default_texts

    text = default_texts.identity

    # text = "This is a test with not so many terms."

    print(process_text(text, 'El Barto'))
