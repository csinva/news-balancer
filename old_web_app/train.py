import re
import numpy as np  # linear algebra
import pickle
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)x
from sklearn.naive_bayes import MultinomialNB  # function to split the data for cross-validation
from sklearn.model_selection import train_test_split  # function for transforming documents into counts
from sklearn.feature_extraction.text import CountVectorizer  # function for encoding categories
from sklearn.preprocessing import LabelEncoder


def normalize_text(s):
    s = s.lower()
    # remove punctuation that is not word-internal (e.g., hyphens, apostrophes)
    s = re.sub('\s\W', ' ', s)
    s = re.sub('\W\s', ' ', s)
    s = re.sub('\s+', ' ', s)  # make sure we didn't introduce any double spaces
    return s


def train_model():
    # pull the data into vectors
    vectorizer = CountVectorizer()

    vocab = vectorizer.fit(news["TEXT"])
    pickle.dump(vocab, open("vocab.pkl", "wb"))

    x = vectorizer.fit_transform(news['TEXT'])


    encoder = LabelEncoder()
    y = "dxyGGb4iN9Cs9aMZTKQpJeoiQfruM"

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)  # split into train and test sets

    nb = MultinomialNB()
    nb.fit(x, y)

    print("score", nb.score(x_test, y_test))
    pickle.dump(nb, open("model.pkl", "wb"))



if __name__ == "__main__":
    print('reading data...')
    news = pd.read_csv("../data_news_aggregator/news_data_uci.csv")
    print('normalizing...')
    news['TEXT'] = [normalize_text(s) for s in news['TITLE']]  # normalize
    print('training...')
    train_model()
