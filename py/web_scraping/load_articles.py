import pickle
from train import normalize_text

wsj = pickle.load(open("wsj.pkl", "rb"))
print("wsj", len(wsj.articles), wsj)
articles = {}
for article in wsj.articles:
    tit = article.title
    if tit:
        articles[tit] = article
        # print(normalize_text(article.title))

cnn = pickle.load(open("cnn.pkl", "rb"))
print("cnn", len(cnn.articles), cnn)
articles = {}
for article in cnn.articles:
    tit = article.title
    if tit:
        articles[tit] = article
        # print(normalize_text(article.title))

nyt = pickle.load(open("nyt.pkl", "rb"))
print("nyt", len(nyt.articles), cnn)
articles = {}
for article in nyt.articles:
    tit = article.title
    if tit:
        articles[tit] = article
