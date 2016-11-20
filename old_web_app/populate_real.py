import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
from myproject.myapp.models import Document
import re
import numpy as np  # linear algebra
import pickle
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)x
from sklearn.naive_bayes import MultinomialNB  # function to split the data for cross-validation
from sklearn.model_selection import train_test_split  # function for transforming documents into counts
from sklearn.feature_extraction.text import CountVectorizer  # function for encoding categories
from sklearn.preprocessing import LabelEncoder
from pubEvaluator import evaluatePubs
import math

def normalize_text(s):
    # s = s.lower()
    # remove punctuation that is not word-internal (e.g., hyphens, apostrophes)
    s = re.sub('\s\W', ' ', s)
    s = re.sub('\W\s', ' ', s)
    s = re.sub('\s+', ' ', s)  # make sure we didn't introduce any double spaces
    return s


if __name__ == '__main__':
    print('reading data...')
    news = pd.read_csv("../data_news_aggregator/news_data_uci.csv")
    news['TEXT'] = [normalize_text(s) for s in news['TITLE']]  # normalize
    # want to use news['TEXT','URL','PUBLISHER']
    pubs = news['PUBLISHER']
    pubs = [p for p in pubs]
    uniquePubs, counts = np.unique(pubs, return_counts=True)
    cred_dict = evaluatePubs(uniquePubs, counts)

    print('populating...')  # 422,419
    bias_arr = np.random.rand(422419, 1)
    cred_arr = np.random.rand(422419, 1)
    for i in range(1000):  # len(news['TEXT'])):
        # print(i)
        pub = news['PUBLISHER'][i]
        if not pd.isnull(pub):
            d = Document(title=news['TEXT'][i], publisher=pub, link=news['URL'][i],
                         cluster=news['STORY'][i], bias=cred_dict[pub][0], cred=cred_dict[pub][1])
            d.save()
    print("done populating...")
