import tensorflow.keras.backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Bidirectional, LSTM, GlobalMaxPool1D
from transformers import DistilBertTokenizer, TFDistilBertModel


def get_base_bert():
    """ Loads the Base BERT Model """

    K.clear_session()
    bert_model = 'distilbert-base-uncased'
    tokenizer = DistilBertTokenizer.from_pretrained(bert_model)
    bert_model = TFDistilBertModel.from_pretrained(bert_model)
    return tokenizer, bert_model


def get_news_classifier():
    """ Loads the News Classification Model """
    news_classifier = Sequential([
        Input(shape=(128, 768)),
        Bidirectional(LSTM(128, dropout=0.2, return_sequences=True)),
        GlobalMaxPool1D(),
        Dense(512, activation='relu'),
        Dense(211, activation='sigmoid')
    ])
    news_classifier.load_weights("models/Weights/Weights")
    return news_classifier
