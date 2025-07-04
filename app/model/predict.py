from app.definitions import ROOT_DIR

import pandas as pd
import keras

import nltk 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re

stop_words = stopwords.words('english')
stemmer = SnowballStemmer('english')
nltk.download('stopwords', quiet=True)
text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

def clean_X(text: str):
    stem=True
    text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)
    return " ".join(tokens)

from keras.preprocessing.sequence import pad_sequences
import pickle

with open(ROOT_DIR / 'app/model/files' / 'tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

def tokenize_X(X: pd.core.series.Series):
    X = X.to_list()
    X = pad_sequences(tokenizer.texts_to_sequences(X), maxlen = 30)
    return X

model = keras.models.load_model(ROOT_DIR / 'app/model/files' / 'model.keras')
encoding = {v: k for k, v in {'joy': 0, 'fear': 1, 'anger': 2, 'sadness': 3}.items()}

def predict(text: str):
    series_text = pd.core.series.Series(clean_X(text))
    output = model.predict(tokenize_X(series_text), verbose=0)
    emotion = encoding[output.argmax()]

    return emotion