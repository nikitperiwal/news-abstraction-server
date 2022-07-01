import constants
import tensorflow.keras.backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Bidirectional, LSTM, GlobalMaxPool1D
from transformers import DistilBertTokenizer, TFDistilBertModel


def get_base_bert():
    """ Loads the Base BERT Model """

    K.clear_session()
    tokenizer = DistilBertTokenizer.from_pretrained(constants.CATEGORY_BASE_BERT)
    bert_model = TFDistilBertModel.from_pretrained(constants.CATEGORY_BASE_BERT)
    return tokenizer, bert_model


def get_news_classifier():
    """ Loads the News Classification Model """
    news_classifier = Sequential([
        Input(shape=(constants.NEWS_MAX_LENGTH, 768)),
        Bidirectional(LSTM(constants.NEWS_MAX_LENGTH, dropout=0.2, return_sequences=True)),
        GlobalMaxPool1D(),
        Dense(32, activation='relu'),
        Dense(constants.NEWS_NUM_OUTPUT, activation='softmax')
    ])
    news_classifier.load_weights(constants.CATEGORY_MODEL_WEIGHT_PATH)
    return news_classifier
