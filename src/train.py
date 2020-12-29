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
    x = vectorizer.fit_transform(news['TEXT'])

    encoder = LabelEncoder()
    y = encoder.fit_transform(news['CATEGORY'])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)  # split into train and test sets

    nb = MultinomialNB()
    nb.fit(x_train, y_train)

    print("score", nb.score(x_test, y_test))
    pickle.dump(nb, open("model.pkl", "wb"))


def sortBy(X, Y):
    return ([x for (y, x) in sorted(zip(Y, X))])


if __name__ == '__main__':
    print('reading data...')
    news = pd.read_csv("../data_news_aggregator/news_data_uci.csv")
    news['TEXT'] = [normalize_text(s) for s in news['TITLE']]  # normalize
    train_model()

    pubs = news['PUBLISHER']
    pubs = [p for p in pubs]
    print(pubs)

    uniquePubs, counts = np.unique(pubs, return_counts=True)

    uniquePubs = sortBy(uniquePubs, counts)
    counts = sorted(counts)

    # PUBLISHER, COUNT, BIAS, CRED
    pubData = pubEvaluator.evaluatePubs(uniquePubs, counts)

    idxs_init = get_related_article_idxs(news['TEXT'][0], news['STORY'][0])
    idxs_liberal = get_liberal_idxs(idxs_init)
    idxs_conservative = get_conservative_idxs(idxs_init)
    idxs_fair = np.logical_and(idxs_init, np.logical_not(np.logical_or(idxs_liberal, idxs_conservative)))
    # print("sums", np.sum(idxs_init), np.sum(idxs_liberal), np.sum(idxs_conservative), np.sum(idxs_fair))
