from models import get_base_bert, get_news_classifier

# Loads the tokenizer and the models
bert_tokenizer, bert_model = get_base_bert()
news_classifier = get_news_classifier()


def tokenize_data(text):
    """
    Tokenizes the passed text and returns a tf tensor.
    """

    tokens = bert_tokenizer(
        text,
        max_length=90,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )
    input_ids, attention_mask = tokens['input_ids'], tokens['attention_mask']
    return [input_ids, attention_mask]


def bert_predict(description):
    """
    Predicts using Base BERT model. Returns the prediction embedding.
    """

    tokens = tokenize_data(description)
    output = bert_model.predict(tokens)[0]
    return output


def predict_category(bert_output, news_categories):
    """
    Returns the category of news by predicting on the bert_output.

    Parameters:
    -----------
    bert_output: tf embedding of the bert output
    news_categories: list of all categories
    """

    pred = news_classifier.predict(bert_output)[0]
    pred_index = pred.numpy().argmax()
    return news_categories[pred_index]
