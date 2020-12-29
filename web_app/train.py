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
    idxs = [False for i in range(len(news['STORY']))]
    idxs = news["STORY"] == "dM5lJS_3o5WVi3Msw6l8yvek3qu2M"
    idxs |= news["STORY"] == "dvXpoeHHC3Eh4CMUx4PxTjcvbPZNM"
    idxs |= news["STORY"] == "dlLYTMlYRD9PexMYGrncsueKjZmMM"
    idxs |= news["STORY"] == "dMPYwYKkTueEQ5MwewRLr9q1Ye6rM"
    idxs |= news["STORY"] == "d2OyTeAXDFQpb3M9Cr_Ftde6Ig0aM"
    for i in range(1000):
        idxs[i] = True

    print(len(idxs))

    tits = []
    stories = []

    for i in range(len(idxs)):
        if (idxs[i]):
            tits.append(news["TEXT"][i])
            stories.append(news["STORY"][i])

    # tits = news["TEXT"][idxs]
    # print("len tits", len(tits))
    # stories = news["STORY"][idxs]
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(tits)
    encoder = LabelEncoder()
    y = encoder.fit_transform(stories)
    pickle.dump(encoder, open("encoder.pkl", "wb"))

    # save voc
    analyze = vectorizer.build_analyzer()
    voc = set(analyze(tits[0]))
    for i in range(len(tits)):
        voc.update(analyze(tits[i]))
    pickle.dump(voc, open("vocab.pkl", "wb"))

    print("x_shape,y_shape", x.shape, y.shape)

    nb = MultinomialNB()
    nb.fit(x, y)

    print("score", nb.score(x, y))
    pickle.dump(nb, open("model.pkl", "wb"))


if __name__ == "__main__":
    print('reading data...')
    news = pd.read_csv("../data_news_aggregator/news_data_uci.csv")
    print('normalizing...')
    news['TEXT'] = [normalize_text(s) for s in news['TITLE']]  # normalize
    print('training...')
    train_model()
