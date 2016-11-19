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
