import constants
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
        max_length=constants.NEWS_MAX_LENGTH,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )
    input_ids, attention_mask = tokens['input_ids'], tokens['attention_mask']
    return [input_ids, attention_mask]


def bert_predict(text_list):
    """
    Predicts using Base BERT model. Returns the prediction embedding.
    """

    tokens = tokenize_data(text_list)
    output = bert_model.predict(tokens)[0]
    return output


def predict_category(news_articles):
    """
    Returns the category of news by predicting on the bert_output.

    Parameters:
    -----------
    bert_output: tf embedding of the bert output
    news_categories: list of all categories
    """

    bert_output = bert_predict(news_articles)
    prediction = news_classifier.predict(bert_output)
    indexes = prediction.argmax(axis=1)
    categories = []
    for index in indexes:
        categories.append(constants.NEWS_CATEGORIES[index])

    return categories
